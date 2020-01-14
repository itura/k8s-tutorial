# k8s-tutorial

This is an introductory tutorial to Kubernetes. It contains a trimmed-down overview of what Kubernetes is and what problems it solves. There are a number of lessons which provide step-by-step instructions to take the provided code and run it in Kubernetes. You should be able to use these as examples when developing the Kubernetes configurations for your production applications. 

This tutorial is intended for developers have written some application code and know generally how to containerize it with Docker.

## Prerequisites

As long as the `docker` and `kubectl` commands work as documented on your machine, you should be able to follow along. 

- docker
- python
- kubernetes
  - for Mac, enable Kubernetes through docker-desktop
  - otherwise, install minikube

## Instructions

Start with `intro.md`. Then, follow the numbered directories, each representing a lesson. Each lesson contains a readme with instructions and some source code to work with. Additionally, each lesson will contain exercises which are not discussed but have proved useful in my practical experience. 

## Recommended Reading

- [Official Kubernetes Concepts](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)
- [Pretty good intro](https://www.bmc.com/blogs/what-is-kubernetes/)
