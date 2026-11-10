import pyopencl as cl
import numpy as np

def part_3():
    with open("Day 6/part 3.txt", "r") as f:
        line = f.readline()
    WORK_GROUP_SIZE = 64
    mentors = np.zeros(len(line) * 3000, dtype=np.int32)
    blocks = np.empty(len(line) * 1500 // WORK_GROUP_SIZE, dtype=np.int32)
    output = np.empty(len(line) * 1000 // (WORK_GROUP_SIZE << 1), dtype=np.int32)
    ctx = cl.create_some_context()

    mf = cl.mem_flags
    mentors_buf = cl.Buffer(ctx, mf.COPY_HOST_PTR | mf.READ_WRITE, hostbuf=mentors)
    blocks_buf = cl.Buffer(ctx, mf.COPY_HOST_PTR | mf.READ_WRITE, hostbuf=blocks)
    output_buf = cl.Buffer(ctx, mf.COPY_HOST_PTR | mf.WRITE_ONLY, hostbuf=output)
    line_buf = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=line.encode())

    queue = cl.CommandQueue(ctx)

    prg = cl.Program(ctx, """
    __kernel void check_mentor(__global int *mentors, __global const char *line, const int n) {
      const int gid = get_global_id(0);
      const char c = line[gid % n];
                     
      if (c <= 'Z') {
        mentors[gid * 3 + c - 'A'] = 1;
      }
    }
                     
    __kernel void prefix_sum(__global int *mentors, __global int *blocks) {
      const int gid = get_global_id(0);
      const int lid = get_local_id(0);
      const int SIZE = 64;
                     
      __local int data[SIZE << 1];
                     
      for (int group = 0; group < 3; ++group) {               
        data[lid * 2] = mentors[gid * 6 + group]; 
        data[lid * 2 + 1] = mentors[gid * 6 + 3 + group];
        int offset = 1;
                     

        for (int d = SIZE; d > 0; d >>= 1) {
          barrier(CLK_LOCAL_MEM_FENCE);
                     
          if (lid < d) {
            int ai = offset * (lid * 2 + 1) - 1;
            int bi = offset * (lid * 2 + 2) - 1;
            data[bi] += data[ai];
                     
          }
          offset <<= 1;
        }
                     
        if (lid == 0) {
            blocks[get_group_id(0) * 3 + group] = data[(SIZE << 1) - 1];
            data[(SIZE << 1) - 1] = 0;
        }
                     
        for (int d = 1; d <= SIZE; d <<= 1) {
          offset >>= 1;
          barrier(CLK_LOCAL_MEM_FENCE);
                     
          if (lid < d) { 
            int ai = offset * (2 * lid + 1) - 1;
            int bi = offset * (2 * lid + 2) - 1;
            int t = data[ai];
                     
            data[ai] = data[bi];
            data[bi] += t;
          }
        }
                     
        barrier(CLK_LOCAL_MEM_FENCE);
        mentors[gid * 6 + group] += data[lid * 2]; 
        mentors[gid * 6 + 3 + group] += data[lid * 2 + 1];
        barrier(CLK_LOCAL_MEM_FENCE);
      }
    }    
                             
    __kernel void add_blocks(__global int *mentors, __global const int *blocks) {
      int gid = get_global_id(0);
                    
      for (int i = 0; i < 3; ++i) {
        mentors[gid * 6 + i] += blocks[get_group_id(0) * 3 + i];
        mentors[gid * 6 + 3 + i] += blocks[get_group_id(0) * 3 + i];
      }
    }
                             
    __kernel void check_students(__global const int *mentors, __global const char *line, __global int *output, const int n) {
      const int gid = get_global_id(0);
      const int lid = get_local_id(0);
      const char c = line[gid % n];
      const int SIZE = 128;
      int offset = 1;
                     
      __local int data[SIZE];
                     
      data[lid] = (c >= 'a')? (mentors[min(gid + 1000, n * 1000 - 1) * 3 + c - 'a'] - ((gid > 1000)? mentors[(gid - 1001) * 3 + c - 'a']: 0)): 0;
      
      for (int d = SIZE >> 1; d > 0; d >>= 1) {
        barrier(CLK_LOCAL_MEM_FENCE);
                    
        if (lid < d) {
          int ai = offset * (lid * 2);
          int bi = offset * (lid * 2 + 1);
          data[ai] += data[bi];
        }
        offset <<= 1;
      }     
      barrier(CLK_LOCAL_MEM_FENCE);
      if (lid == 0) output[get_group_id(0)] = data[0];
    }
    """).build()


    prg.check_mentor(queue, (len(line) * 1000,), None, mentors_buf, line_buf, np.int32(len(line)))
    prg.prefix_sum(queue, (len(line) * 500,), (WORK_GROUP_SIZE,), mentors_buf, blocks_buf)
    
    cl.enqueue_copy(queue, blocks, blocks_buf)

    for i in range(3):
        total = 0
        for j in range(i, len(blocks), 3):
            t = blocks[j]
            blocks[j] = total
            total += t
  
    cl.enqueue_copy(queue, blocks_buf, blocks)
    prg.add_blocks(queue, (len(line) * 500,), (WORK_GROUP_SIZE,), mentors_buf, blocks_buf)
    prg.check_students(queue, (len(line) * 1000,), (WORK_GROUP_SIZE << 1,), mentors_buf, line_buf, output_buf, np.int32(len(line)))

    cl.enqueue_copy(queue, output, output_buf)

    ans = output.sum()
    return ans

# import time
# t = time.time()
# part_3()
# print(time.time() - t)

import timeit

print(timeit.timeit(part_3, number=10) / 10)
