Hi there, I'm [husharp](https://github.com/HuSharp)👋

This organization contains the collection of my toy projects during learning. Some of them might be helpful.

### Some highlights (incomplete unordered list):

- [jsonParser](https://github.com/ihusharp/jsonParser/tree/master/Json_stu/tutorial08): A tiny JSON parser. This was my first exposure to engineering. It's a very friendly project development tutorial for novices and sparked my interest in engineering 

- [UnixImpl](https://github.com/ihusharp/Unix-Linux_Programming#unix-linux_programming): inspired by understanding-unix-programming

- [tiny KV](https://github.com/ihusharp/talent-plan_tinykv): A tiny key-value store, and builds a key-value storage system with the Raft consensus algorithm. It is inspired by [MIT 6.824](https://pdos.csail.mit.edu/6.824/) and [TiKV Project](https://github.com/tikv/tikv). After completing this, I have the knowledge to implement a horizontally scalable, highly available, key-value storage service with distributed transaction support :)

- **[tiny OS](https://github.com/ihusharp/HuSharp_OS)**: A tiny operating system. Complete the filling of Tsinghua [uCoreOS_labs](https://github.com/ihusharp/uCoreOS_labs), and refer to [The truth about operating systems](https://book.douban.com/subject/26745156/) to impl a simple operating system on bochs, the main contents are: 

  - kernel thread, user process, fork and execv, task scheduling;  
  - interrupts (clock, keyboard, hard disk, system call, etc.), memory management, file system, shell, pipeline; 
  - binary semaphore based locks, file system, and so on.

  Approximately 6323 lines of valid code, using knowledge of c/c++, assembly, bochs debugging, and Unix system programming.

- **[Tity MIPS CPU](https://github.com/ihusharp/hust_MIPS_CPU_Design)**: Utilizing knowledge of combinational logic and synchronous timing logic circuit design, start with logic gates and gradually build operators, memories, datapaths, and controllers, ultimately integrating them into a complete CPU prototype system. Inspired by [Computer Composition Principle](https://book.douban.com/subject/35379794/).

And I use different languages for writing code, especially Go & Rust.

### Some Go Impl

- [Tiny Interpreter](https://github.com/ihusharp/Go-practice/tree/master/Interpreter) Inspired by  [Writing an interpreter in go](https://interpreterbook.com/): building a inteepreter which named Monkey. It has a C-like syntax, supports **variable bindings**, **prefix** and **infix** operators, has **first-class and higher-order functions**, can handle **closures** with ease and has **integers**, **booleans**, **arrays** and **hashes** built-in.

- [Tiny Compiler](https://github.com/ihusharp/Go-practice/tree/master/Compiler) Inspired by  [Writing a compiler in go](https://compilerbook.com/): It's the next step in Monkey's evolution. We’re going to turn our tree-walking and on-the-fly-evaluating interpreter into a bytecode compiler and a virtual machine that executes the bytecode. And test for interpreter with compiler for the fibonacci.

  ```
  $ ./fibonacci -engine=eval
  engine=eval, result=9227465, duration=11.327551667s
  
  $ ./fibonacci -engine=vm
  engine=vm, result=9227465, duration=3.907876125s
  ```

- [Some Others](https://github.com/geektutu/7days-golang)

  - [Web Framework - GeeHTTP](https://github.com/ihusharp/Go-practice/blob/master/GeeHTTP)

  - [Distributed Cache - GeeCache](https://github.com/ihusharp/Go-practice/blob/master/GeeCache)

  - [Object Relational Mapping - GeeORM](https://github.com/ihusharp/Go-practice/blob/master/GeeORM)

  - [RPC Framework - GeeRPC](https://github.com/ihusharp/Go-practice/blob/master/GeeRPC)

### Some Rust Impl

- [Tokio](https://tokio.rs/tokio/tutorial): This tutorial will take you step by step through the process of building a [Redis](https://redis.io/) client and server. We will start with the basics of asynchronous programming with Rust and build up from there. We will implement a subset of Redis commands but will get a comprehensive tour of Tokio.
- [Hecto](https://www.flenker.blog/hecto/): This is a series of blog posts that shows you how to build a text editor in Rust. It’s a re-implementation of [kilo](http://antirez.com/news/108) in Rust, as outlined in [this fantastic tutorial](https://viewsourcecode.org/snaptoken/kilo/index.html). Same as the original booklet, these blog posts guide you through all the steps to build a basic text editor, `hecto`.
- [Lists](https://rust-unofficial.github.io/too-many-lists/): This is a series of how to implement a linked list in Rust. The answer honestly depends on what your requirements are, and it's obviously not super easy to answer the question on the spot. As such I've decided to write this book to comprehensively answer the question once and for all.
- [Writing an OS in Rust](https://os.phil-opp.com/): This blog series creates a small operating system in the [Rust programming language](https://www.rust-lang.org/). Each post is a small tutorial and includes all needed code, so you can follow along if you like. The source code is also available in the corresponding [repository](https://github.com/phil-opp/blog_os).

