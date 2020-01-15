"kubernetes" is greek for "pilot of a ship". The tool Kubernentes (or k8s) is hard to describe succinctly because of its scope and the large ecosystem surrounding the tool. I recommend reading the [official docs](https://kubernetes.io/docs/concepts/) for the authoritative description. I will attept to provide a more compact introduction more oriented towards framing the usage of the tool rather than explaining what it does in detail.

## Definitions

Many Kubernetes concepts are things we are familiar with, just more generic. Additionally, the space is filled with overloaded terms. I will begin by providing my own definitions for common infrastructure terms:

We begin by defining an "application", which is an amorpheous term made worse by "app". For our purposes, we will use these definitions:
- application: an executable computer program which can take the following forms:
  - script: series of commands that can be run repeatedly
  - service, server: persistent, stateless application exposed via HTTP
  - microservice: "small" service likely dependent on other "small" services
  - database: store for persistent data
  - daemon: runs in the background and fowards requests to workers/agents
  - message queue: mechanism for processing and delivering events
  - data pipeline: distributed, highly parallelized content ingestion system

All these types of applications and more have to be coded on a developer's workstation, and then delivered to a cloud-based production environment. Throughout this process, applications will likely have to be executed on many different types of computers, for which we will use the following definitions:

- computer: "bare metal" CPU, memory, disk, etc all wired together
- operating system: an application which allows other applications to leverage the computer hardware
- virtual machine: an application which provides emulated hardware for an operating system to run on
- container: a snapshot of an execution context which can be run as an application
- host: bare metal or virtual computer running an application

This brings us to terms relating to the delivery infrastructure for our application:

- artifact: a validated, releasable version of an application (typically a container)
- CI: system which continuously integrates changes in source code/assets into new artifacts
- deploy: to stand up a host in the desired environment and run an artifact on it
- CD: system which continuously deploys new, validated artifacts
- replica: additional host of a load-balanced application
- scaling: process of changing the number of replicas or the allocated resources of an application

## The goal
With these terms, we can say that our goal is to develop an application with a team of developers and continuously build and deploy new artifacts for all changes that occur, without incurring any downtime. Additionally, we want a reliable and low-friction mechanism to scale the system for both traffic and and operational expense. 

## What is Kubernetes?
We will now discuss what Kubernetes is and how it helps us achieve the aims we have laid out. I will continue to use the above terms as a basis, and try to emphasize Kubernetes-specific terminology with capitalization to help distinguish between overloaded words.

Kubernetes is a tool centered around "production-grade container orchestration". When the artifacts of your application are containers, you can use Kubernetes to centrally provision resources, schedule and scale your applications as "workloads", and provide networking. Assuming you can continuously produce new containers, Kubernetes lets you seamlessly deploy changes with little to no downtime. It eases the overhead of managing a distributed system, and internal networking makes it easy for applications to find each other.

Kubernetes itself takes the form of a distributed cluster responsible for running, tracking, and connecting arbitrary applications. A cluster consists of two or more hosts called Nodes. One Node in the cluster is the Kubernetes Master, which governs the scheduling of workloads, tracking of system state, and exposure of the Kubernetes API Server. The latter is used to administrate the cluster, typically via the `kubectl` command line interface. API Server endpoints allow you to schedule and manage workloads across the non-master Nodes in the cluster, as well as to inspect detailed information about each resource in the cluster.

![Control Plane](./pictures/k8s-cluster-1.png "Control Plane")

Users of the API Server submit their desired state of the cluster, causing the Kubernetes Master to determine what changes will be needed to achieve the desired state. The Kubernetes Master will communicate to `kubelet` agent processes running on non-master Nodes to determine the best way to apply the changes. `kubelet` processes control a container runtime, and are eventually responsible for running containers on the Node. This system of communication is referred to as the Control Plane.

There's a lot to take in about what Kubernetes does and how. I think that it helps to be exposed to the concepts, then get some hands-on time working with the tool, then return to the concepts with a better understanding of what you need from Kubernetes. 

Working knowledge about Kubernetes revolves around interactions with the API Server. Most of the content from here will focus on describing different parts of the API and how to use them to achieve certain goals.

