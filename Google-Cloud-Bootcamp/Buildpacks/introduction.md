# Buildpacks 

Buildpacks are tools that automatically build container images (Docker images) for your application without you writing a Dockerfile.

You give them your source code, and they: 

- Detect what language or framework your app uses (like Node.js, Python, Java, etc.),

- Install all dependencies,

- Set up the runtime environment,

- Build and package your app into a container image ready to run in the cloud.

So — instead of doing all this manually in a Dockerfile, buildpacks do it for you automatically.