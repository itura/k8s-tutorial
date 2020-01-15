# 01: Pods

The first Kubernetes API Object that we will dive into is the Pod. At a high level, the Pod resource is how we request CPU and memory resources, and assign a container to run on those resources. The Pod resource forms the basis for most other types of resources you can create in Kubernetes. In reality, a single Pod can execute multiple different containers with the same resources as well as provide storage, but for introductory purposes we will assume a Pod is simply a vessel for a single container using no storage.

Recall the diagram of the of the Kubernetes Control Plane:

![Control Plane](../pictures/k8s-cluster-1.png "Control Plane")

When we submit Pod definitions to the API Server running on the Kubernetes Master, it will work with its `kubelet` agents to determine which Node to schedule the pod on, then that Node's `kubelet` agent will execute the work in its container runtime.

To illustrate, we will take a dead-simple python script and run it in three different contexts: locally, in a container, and in a Kubernetes cluster. 

## Local

Most computers with a bash shell ship with some version of Python. While you should be using 3 by now, the 2.7 version shipped by default on many machines should suffice for this example.

```bash
cd 01/app
python -m hello_world # -> Hello World
HELLO_WHAT="The Great Beyond" python -m hello_world # -> Hello The Great Beyond
```

## Container

Before running these commands, take a look through `01/app/Dockerfile`. If it's not self-explanatory, please read up on building docker images and running them as containers. Note that this Dockerfile uses an alpine base image, which is missing many of the command-line niceties we are used to.

```bash
cd 01
docker build -t hw:latest app/
docker run -ti --rm hw:latest # -> Hello World
docker run -ti --rm -e HELLO_WHAT="The Great Beyond" hw:latest # -> Hello The Great Beyond

# Optionally, inspect the folder structure of the container by running sh instead of the CMD given in the Dockerfile
docker run -ti --rm hw:latest /bin/sh
```

## Kubernetes

Now for the main event! It's assumed that by now you successfully executed all the commands in the previous section. Most importantly, you should have built an image using `01/app/Dockerfile` and tagged it as `hw:latest`. This isn't just a detail of this tutorial; Kubernetes uses container images and configuration as input. I've provided the configuration, but it's up to you to provide the image. There are two k8s manifests in `01/config`, and both specify `hw:latest` as the image to run in the Pod (and they expect it to be the one defined in the Dockerfile).

We will use `kubectl` as an interface to the Kubernetes API Server, and submit both of our manifests in turn. Each manifest is a minimal definition of a Pod, and when we submit these descriptions with `kubectl apply`, the API Server will attempt to create and run the Pod defined in the manifest. Our Pod is simple enough that it should create and run in the blink of an eye, but keep in mind the types of containers we will try to be running for our production applications.

```bash
cd 01
kubectl apply -f config/pod.yaml # -> pod/hello-world-pod created
kubectl logs pod/hello-world-pod # -> Hello World
kubectl describe pod/hello-world-pod # ...
kubectl delete pod/hello-world-pod # -> pod "hello-world-pod" deleted

kubectl apply -f config/pod-with-env.yaml # -> pod/hello-world-pod created
kubectl logs pod/hello-world-pod # -> Hello The Great Beyond
kubectl describe pod/hello-world-pod # ...
kubectl delete pod/hello-world-pod # -> pod "hello-world-pod" deleted
```

While not necessary, it's encouraged to describe the two pods that are created and find the configuration you have specificed. If you're savvy, you may be able to glean some information from the configuration which was applied that we didn't provide in our manifests.

A couple notes on the manifests:
- the value provided for `metadata.name` is the value which we will use to interact with the resource via `kubectl`.
- we have not provided any values for `metadata.labels`. Kubernetes and associated tools use labels for a variety of functionality. We have excluded them for simplicity, but keep in mind that labelling is an important mechanism for both simple and advanced features of Kubernetes.
- the value provided for `spec.containers.0.image` must be available to the container runtime. On our local machines, this just means that you must have built the image with your local container runtime. In the cloud, the image must exist in the image repository associated with your container runtime. 

## Conclusion

What stands out immediately is that running this code in Kubernetes is a lot harder than running it on your local machine. Granted, this code is not the type of stuff that we need "production grade container orchestration" for. However, the relative difficulty of running code in Kubernetes will be an ongoing pattern. Eventually this pattern will lead us to other tools which have been built on top of Kubernetes in order to provide saner developer workflows. 

But for now, understanding the basics of how Pods are submitted to the API Server and scheduled on Nodes is a fundamental building block of our working knowledge. The Pod API used in these manifests will be leveraged as a part of larger APIs used to schedule more complicated pieces of work.

Additionally, Kubernetes will run its own system Pods in order to provide the full functionality of a Kubernetes cluster. This is one of the confusing parts about Kubernetes: It's not just a bunch of connected hosts with container runtimes, it's that AND a small set of system processes which run on the very same infrastructure that we leverage with our manifests.

In the next section we will explore some of these system processes, through which we'll discover the Kubernetes resources called Services. Ever wish you could access an application in your system via http://hello-world.com? Well, welcome to the future.

## PS: Security
While this configuration is easy to deploy to Kubernetes, it is also easy to exploit. Application developers generally don't need to be security experts, but we should definitely work in tandem with them. The platform engineering group which is providing your Kubernetes cluster should provide rules and guidelines, likely including CVE scanning, non-root images, and resource limits. Don't deploy to production without someone understanding the risks.

Security (and container security) is a topic in its own right, and will not be emphasized here. As you learn, keep in mind that you will have to take into account the security concerns that more knowledgable people put forth.

## References
Start [here](https://kubernetes.io/docs/concepts/workloads/pods/pod-overview/). Go back frequently.

## Exercises
1. Create a hello world app in a language other than python and run it in kubernetes
1. Deploy multiple pods which run the same container
1. Deploy a pod with multiple containers
1. Inject the HELLO_WHAT parameter via command line args instead of as an environment variable

