### Scala

Scala (short for Scalable Language) is a modern, statically typed, general-purpose programming language that blends object-oriented and functional programming paradigms. It was designed by Martin Odersky in 2003–2004 to address limitations of Java while remaining fully interoperable with it.

### How It Works
Scala compiles source code into JVM bytecode, meaning it runs on the Java Virtual Machine just like Java. This gives it access to the entire Java ecosystem — libraries, frameworks, and tooling — without being an extension of Java itself. It also supports JavaScript runtimes via Scala.js.

### What Scala Is Used For
Scala is heavily used in Big Data and distributed systems, being the language behind Apache Spark, Kafka, and Flink. Its strong type safety and functional features also make it popular for building complex, data-intensive backend services.


### scalac — The Raw Compiler
scalac is the Scala Compiler. It does one job only — takes your .scala file and converts it into .class bytecode files that the JVM can run. 

### scala-cli — The All-in-One Tool
scala-cli is a modern tool that wraps scalac and does everything for you — compile, run, manage dependencies, manage Scala versions.

As of Scala 3.5.0, scala-cli became the official way to run Scala — it replaced the old scalac + scala manual workflow.

