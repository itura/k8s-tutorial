# 03: Storage

So far, we've covered how to use `kubectl` and YAML manifests to deploy simple, stateless applications with access to CPU, memory, and networking. The last computing resource we need to learn to request from Kubernetes is storage, which will enable deploying applications such as databases.

The base Kubernetes API Object we are concerned with is the Volume, which provides persistent storage for a Pod. When a Pod has a Volume, any containers (re-)started in the Pod will have access to the Volume. There are many different types of Volumes, each allowing you to mount a different type of device ranging from a local directory to a cloud-provided volume (eg. EBS).

In our basic example, we will configure a Volume and attach it directly to a Pod. One limitation of this approach is that the Volume will disapper once the Pod is deleted, but we will deal with this problem later.

This iteration of hello-world is a web server that, upon each request, will write the line "Hello World" to a file `/data/hello.txt`, then respond with all the lines in the file. Look through `config/hello-world.yaml` to see how we configure the Kubernetes Volume to point to a directory we will create.


```bash
cd 03/

# create directory to use for volume
mkdir /tmp/hello-data

# build images
docker build -t hw:latest hello-world/

# hello-world
kubectl apply -f config/hello-world.yaml
kubectl port-forward service/hello-world-service 8080:8080

# In another session
curl localhost:8080
# -> Hello World

curl localhost:8080
# -> Hello World
#    Hello World

cat /tmp/hello-data/hello.txt
# -> Hello World
#    Hello World
```

We've illustrated that the hello-world application has access to the specified directory, and that the data in that directory will be persisted. Now, we will show that the Volume will persist across container failures. We fake a container failure by manually stopping the container.

```bash
docker ps # -> copy container id from this output
docker stop [container id]

kubectl get all # -> see that everything is still running
docker ps # -> see that a different container is running now
kubectl port-forward service/hello-world-service 8080:8080

# In another session
curl localhost:8080
# -> Hello World
#    Hello World
#    Hello World

cat /tmp/hello-data/hello.txt
# -> Hello World
#    Hello World
#    Hello World
```

While this example shows how to configure an application to use a specific type of volume, we often want Kubernetes to figure out which specific type of device to use. For example, we'd like the volume to be provisioned from a local directory on our workstations, but we'd also like the volume to be provioned from EBS when our cluster is hosted on AWS. We can achieve this flexibility without duplicating configuration using two more Kubernetes API Objects called PersistentVolume and PersistentVolumeClaim.



There are 2 Kubernetes API Objects used when dealing with storage: PersisentVolume and PersistentVolumeClaim. The former represents the actual storage device, while the latter is a request for a storage device with certain properties, such as filesystem type or amount of space. 


https://kubernetes.io/docs/tasks/configure-pod-container/configure-persistent-volume-storage/



