import pyopencl as cl
import numpy as np
from collections import deque

def part_3():
    with open("Day 9/part 3.txt", "r") as f:
        lines = [s[s.index(":") + 1:] for s in f.read().splitlines()]
        DNA_LENGTH = np.int32(len(lines[0]))
        PARENT_LENGTH = len(lines)

    parents = np.empty(PARENT_LENGTH << 1, dtype=np.int32)
    ctx = cl.create_some_context()

    mf = cl.mem_flags
    dna_buf = cl.Buffer(ctx, mf.COPY_HOST_PTR | mf.READ_ONLY, hostbuf="".join(lines).encode())
    parents_buf = cl.Buffer(ctx, mf.COPY_HOST_PTR | mf.WRITE_ONLY, hostbuf=parents)

    queue = cl.CommandQueue(ctx)

    prg = cl.Program(ctx, """
    __kernel void find_parents(__global int *parents, __global const char *dnas, const int dna_length, const int parent_length) {
      const int gid = get_global_id(0);
      
      for (int p1 = 0; p1 < parent_length - 1; ++p1) {
        if (p1 == gid) continue;
        for (int p2 = p1 + 1; p2 < parent_length; ++p2) {
          if (p2 == gid) continue;
          bool same = true;
          
          for (int i = 0; i < dna_length; ++i) {
            if (dnas[gid * dna_length + i] != dnas[p1 * dna_length + i] && dnas[gid * dna_length + i] != dnas[p2 * dna_length + i]) {
              same = false;
              break;
            }
          }

          if (same) {
            parents[gid * 2] = p1;
            parents[gid * 2 + 1] = p2;
            return;
          } else {
            parents[gid * 2] = -1;
            parents[gid * 2 + 1] = -1;
          }
        }
      }
    }
    """).build()

    prg.find_parents(queue, (PARENT_LENGTH,), None, parents_buf, dna_buf, DNA_LENGTH, np.int32(PARENT_LENGTH))
    cl.enqueue_copy(queue, parents, parents_buf)

    sizes = [[] for _ in range(PARENT_LENGTH)]

    for ch in range(PARENT_LENGTH):
        p1 = parents[ch << 1]
        p2 = parents[(ch << 1) + 1]
        if p1 < 0: continue

        sizes[p1].append(ch)
        sizes[p2].append(ch)
        sizes[ch].append(p1)
        sizes[ch].append(p2)

    seen = [False] * PARENT_LENGTH
    ans = (0, 0)

    for i in range(PARENT_LENGTH):
        if seen[i]: continue
        seen[i] = True
        size = 0
        total = 0
        queue = deque((i,))

        while queue:
            j = queue.popleft()

            size += 1
            total += j
            
            for k in sizes[j]:
                if seen[k]: continue
                seen[k] = True
                queue.append(k)

        ans = max(ans, (size, total))

    print(sum(ans))

part_3()
