import pyopencl as cl
import numpy as np
import re

def part_3():
  with open("Day 2/part 2.txt", "r") as f:
      res = re.search(r"\[(-?\d+),(-?\d+)\]", f.read())
      A = (int(res.group(1)), int(res.group(2)))

  output = np.empty(1001 * 1001, dtype=np.bool)

  ctx = cl.create_some_context()
  queue = cl.CommandQueue(ctx)

  o_buf = cl.Buffer(ctx, cl.mem_flags.WRITE_ONLY, output.nbytes)

  prg = cl.Program(ctx, """

  __kernel void loop(
      __global bool *z_g, const int ax, const int ay)
  {
    int gid = get_global_id(0);
    const long a1 = ax + (gid % 1001);
    const long a2 = ay + gid / 1001;
    long r1 = 0;
    long r2 = 0;

    for(uint i=0; i < 100; ++i) {
      const long temp = (((r1 + r2) * (r1 - r2)) / 100000) + a1;
      r2 = (r1 * r2) / 50000 + a2;
      r1 = temp;

      if (r1 < -1000000 || r1 > 1000000 || r2 < -1000000 || r2 > 1000000) {
        z_g[gid] = false;
        return;
      }
    }
                  
    z_g[gid] = true;
    
  }
  """).build()

  prg.loop(queue, output.shape, None, o_buf, np.int32(A[0]), np.int32(A[1]))

  cl.enqueue_copy(queue, output, o_buf)

  print(output.sum())

part_3()