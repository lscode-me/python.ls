# Streams, IPC & Unix Sockets - Resources

## Core Documentation and Manuals

### System Programming References
- [Linux Programming Interface](https://man7.org/tlpi/) - Comprehensive guide to Linux/Unix system programming
- [Advanced Programming in the UNIX Environment](https://www.apuebook.com/) - Classic systems programming textbook
- [Linux System Programming](http://oreilly.com/catalog/9780596009588/) - Practical guide to Linux system calls

### Man Pages - Essential Reading
- [mkfifo(3)](https://man7.org/linux/man-pages/man3/mkfifo.3.html) - Create named pipes (FIFOs)
- [pipe(2)](https://man7.org/linux/man-pages/man2/pipe.2.html) - Create pipe for IPC
- [socket(2)](https://man7.org/linux/man-pages/man2/socket.2.html) - Create communication endpoint
- [unix(7)](https://man7.org/linux/man-pages/man7/unix.7.html) - Unix domain sockets
- [mq_overview(7)](https://man7.org/linux/man-pages/man7/mq_overview.7.html) - POSIX message queues
- [shm_overview(7)](https://man7.org/linux/man-pages/man7/shm_overview.7.html) - Shared memory overview
- [sem_overview(7)](https://man7.org/linux/man-pages/man7/sem_overview.7.html) - POSIX semaphores
- [signal(7)](https://man7.org/linux/man-pages/man7/signal.7.html) - Signal overview

### Tutorials and Guides
- [Beej's Guide to Unix IPC](https://beej.us/guide/bgipc/html/) - Excellent tutorial on Unix IPC mechanisms
- [Linux Journal: IPC Introduction](https://www.linuxjournal.com/article/2156) - Comprehensive IPC overview
- [Unix Pipes Tutorial](https://www.rozmichelle.com/pipes-forks-dups/) - Understanding pipes and process communication
- [Socket Programming in C](https://www.geeksforgeeks.org/socket-programming-cc/) - Practical socket examples

## Programming Resources

### Python IPC Libraries
- [subprocess module](https://docs.python.org/3/library/subprocess.html) - Spawning new processes
- [multiprocessing module](https://docs.python.org/3/library/multiprocessing.html) - Process-based parallelism
- [asyncio subprocess](https://docs.python.org/3/library/asyncio-subprocess.html) - Asynchronous process management
- [signal module](https://docs.python.org/3/library/signal.html) - Signal handling
- [os module](https://docs.python.org/3/library/os.html) - Operating system interface
- [sys module](https://docs.python.org/3/library/sys.html) - System-specific parameters
- [socket module](https://docs.python.org/3/library/socket.html) - Low-level networking interface

### C/C++ Resources
- [GNU libc manual](https://www.gnu.org/software/libc/manual/) - Standard C library documentation
- [System V IPC](https://linux.die.net/man/2/shmget) - Message queues, semaphores, shared memory
- [POSIX threads](https://computing.llnl.gov/tutorials/pthreads/) - Thread programming tutorial

## Advanced Topics and Research

### Performance and Optimization
- [Zero-copy networking](https://www.linuxjournal.com/article/6345) - High-performance data transfer
- [epoll(7) man page](https://man7.org/linux/man-pages/man7/epoll.7.html) - I/O event notification
- [io_uring](https://kernel.dk/io_uring.pdf) - Modern async I/O interface
- [NUMA considerations](https://www.kernel.org/doc/html/latest/vm/numa.html) - Non-uniform memory access

### Security and Isolation
- [Linux namespaces](https://man7.org/linux/man-pages/man7/namespaces.7.html) - Process isolation mechanisms
- [Linux capabilities](https://man7.org/linux/man-pages/man7/capabilities.7.html) - Fine-grained privileges
- [seccomp](https://man7.org/linux/man-pages/man2/seccomp.2.html) - Secure computing mode
- [AppArmor](https://gitlab.com/apparmor/apparmor/-/wikis/Documentation) - Application security

### Container Technologies
- [Docker internals](https://docs.docker.com/engine/) - Container runtime
- [runc specification](https://github.com/opencontainers/runc) - OCI runtime
- [LXC documentation](https://linuxcontainers.org/lxc/documentation/) - Linux containers

## Tools and Utilities

### Debugging and Analysis
- [strace(1)](https://man7.org/linux/man-pages/man1/strace.1.html) - Trace system calls
- [ltrace(1)](https://man7.org/linux/man-pages/man1/ltrace.1.html) - Trace library calls
- [gdb](https://www.gnu.org/software/gdb/documentation/) - GNU debugger
- [perf](https://perf.wiki.kernel.org/index.php/Tutorial) - Performance analysis tool
- [tcpdump/Wireshark](https://www.tcpdump.org/) - Network packet analysis

### Process Management
- [htop/top](https://htop.dev/) - Interactive process viewer
- [ps command guide](https://www.cyberciti.biz/faq/show-all-running-processes-in-linux/) - Process status
- [kill and killall](https://www.computerhope.com/unix/ukill.htm) - Process termination
- [nohup and screen](https://www.computerhope.com/unix/unohup.htm) - Background process management

## Courses and Books

### Online Courses
- [Linux System Programming Specialization (Coursera)](https://www.coursera.org/specializations/linux-system-programming)
- [Systems Programming (edX)](https://www.edx.org/learn/computer-programming/systems-programming)
- [Operating Systems course materials](https://pages.cs.wisc.edu/~remzi/OSTEP/) - Free online book

### Recommended Books
- "Linux System Programming" by Robert Love
- "The Linux Programming Interface" by Michael Kerrisk
- "Advanced UNIX Programming" by Warren W. Gay
- "Unix Network Programming" by W. Richard Stevens
- "Understanding the Linux Kernel" by Daniel P. Bovet

## Community and Forums

### Discussion Forums
- [Linux Questions](https://www.linuxquestions.org/) - Active Linux community
- [Stack Overflow - Linux](https://stackoverflow.com/questions/tagged/linux) - Programming questions
- [Reddit r/linux](https://www.reddit.com/r/linux/) - General Linux discussions
- [Unix & Linux Stack Exchange](https://unix.stackexchange.com/) - System administration

### Mailing Lists
- [Linux Kernel Mailing List](https://lore.kernel.org/lkml/) - Kernel development
- [GNU/Linux discussion lists](https://www.gnu.org/software/mailman/mailman-admin/node12.html)

## Standards and Specifications

### POSIX Standards
- [IEEE POSIX.1-2017](https://pubs.opengroup.org/onlinepubs/9699919799/) - Latest POSIX standard
- [Single UNIX Specification](https://www.opengroup.org/membership/forums/platform/unix) - Unix standards
- [Linux Standard Base](https://wiki.linuxfoundation.org/lsb/start) - Linux distribution standards
