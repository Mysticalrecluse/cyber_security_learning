# Introduction
## Welcome to FreeBSD!
FreeBSD is an Open Source, <mark style="background-color: tomato" title="符合标准">standards-compliant</mark> Unix-like operating system for x86 (both 32 and 64 bit), ARM, AArch64, RISC-V, POWER, and PowerPC computers. It provides all the features that are nowadays <mark style="background-color: tomato" title="take for: 被认为是...; 整体：理所当然">taken for granted</mark>, such as preemptive multitasking, memory protection, virtual memory, multi-user facilities, SMP support, all the Open Source development tools for different languages and frameworks, and desktop features centered around X Window System, KDE, or GNOME. Its particular strengths are:

- <b title="自由主义的">Liberal</b> Open Source license, which grants you rights to freely modify and extend its source code and <b title="包含，合并">incorporate</b> it in both Open Source projects and closed products without imposing <b title="限制">restrictions</b> typical to copyleft licenses, as well as avoiding <b title="潜在的">potential</b> license <b title="不兼容">incompatibility</b> problems.

- Strong TCP/IP networking - FreeBSD implements industry standard protocols with ever increasing performance and <b title="可扩展性">scalability</b>. This makes it a good match in both server, and routing/firewalling roles - and indeed many companies and <b title="供应商">vendors</b> use it <b title="恰恰">precisely</b> for that purpose.

- Fully <b title="集成">integrated</b> OpenZFS support, including root-on-ZFS, ZFS Boot Environments, fault management, administrative delegation, support for jails, FreeBSD specific documentation, and system installer support.

- <b title="广泛的">Extensive</b> security features, from the <b title="强制">Mandatory</b> Access Control framework to Capsicum capability and sandbox <b title="机制">mechanisms</b>.

- Over 30 thousand prebuilt packages for all supported architectures, and the Ports Collection which makes it easy to build your own, customized ones.

- Documentation - in addition to the Handbook and books from different authors that cover topics ranging from system administration to kernel internals, there are also the man(1) pages, not only for userspace daemons, utilities, and configuration files, but also for kernel driver APIs (section 9) and individual drivers (section 4).

- Simple and consistent repository structure and build system - FreeBSD uses a single repository for all of its components, both kernel and userspace. This, along with a unified and easy to customize build system and a well thought-out development process makes it easy to integrate FreeBSD with build infrastructure for your own product.

- <mark style="background-color: tomato" title="忠于...">Staying true</mark> to Unix philosophy, preferring <b title="可组合性">composability</b> instead of <b title="整体式的">monolithic</b> "all in one" daemons with hardcoded behavior.

- Binary <b title="兼容性">compatibility</b> with Linux, which makes it possible to run many Linux binaries without the need for virtualisation.

FreeBSD is based on the 4.4BSD-Lite release from Computer Systems Research Group (CSRG) at the University of California at Berkeley, and carries on the <b title="杰出的">distinguished</b> tradition of BSD systems development. In addition to the fine work provided by CSRG, the FreeBSD Project has put in many thousands of man-hours into extending the functionality and fine-tuning the system for maximum performance and reliability in real-life load situations. FreeBSD offers performance and reliability on par with other Open Source and commercial offerings, combined with cutting-edge features not available anywhere else.
