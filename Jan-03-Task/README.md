## Kubernetes Job & Docker Bind Mount – Complete Workflow

---


#  Question 2  
## Job (Run to Completion)

---

## Problem Statement

### YAML Manifest
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: once-job
spec:
  template:
    spec:
      restartPolicy: Never
      containers:
      - name: worker
        image: busybox:latest
        imagePullPolicy: IfNotPresent
        command: ["sh", "-c", "echo hello from job && sleep 10"]
  backoffLimit: 2
```

### Tasks
- Run job  
- Show job and pod states  
- Explain Completed state  
- Re-run job  

---

## Objective

To demonstrate how a **Kubernetes Job** executes a **one-time task**, ensures completion, and exits successfully.

---

## Workflow (End-to-End)

```
kubectl apply
   ↓
Kubernetes API Server
   ↓
Job Controller
   ↓
Pod Created
   ↓
Container Executes Command
   ↓
Command Completes
   ↓
Pod → Completed
   ↓
Job → Succeeded (1/1)
```

---

## Execution Steps

### Run the Job
```bash
kubectl apply -f once-job.yaml
```

### Show Job State
```bash
kubectl get jobs
```

### Show Pod State
```bash
kubectl get pods
```

### Explain Completed State

- Command finished successfully
- Exit code = 0
- Pod marked as **Completed**
- Job marked as **Succeeded**

### View Logs
```bash
kubectl logs job/once-job
```

### Re-run the Job
```bash
kubectl delete job once-job
kubectl apply -f once-job.yaml
```

### Screenshot
<img width="1312" height="915" alt="Screenshot 2026-01-02 202952" src="https://github.com/user-attachments/assets/5d0de60c-ace5-454a-ad5e-b475f9c28a1f" />

<br>
<br>

---

#  Question 4  
## Editing Static Page Content without Rebuilding Image

---

## Scenario 

A static webpage hosted in Docker contains spelling errors. Instead of rebuilding the image repeatedly, a bind mount is used to edit the page live.

---

## Tasks 

1. Run nginx/httpd container using bind mount  
2. Edit HTML file locally  
3. Refresh browser without recreating container  
4. Confirm updated page content appears  

---

## Objective

To demonstrate **Docker bind mounts** and live-editing of static content.

---

## Workflow (End-to-End)

```
Local HTML File
   ↓
Bind Mount (-v)
   ↓
Nginx Container
   ↓
Browser (localhost:8080)
   ↓
Edit File Locally
   ↓
Refresh Browser
   ↓
Changes Appear
```

---

## Execution Steps

### Create Web Content
```bash
mkdir web-content
cd web-content
nano index.html
```

### Run Container
```bash
docker run -d   --name web-demo   -p 8080:80   -v $(pwd):/usr/share/nginx/html   nginx
```

### Open Browser
```bash
http://localhost:8080
```

### Edit File & Refresh Browser

- Edit index.html locally
- Refresh browser
- Updated content appears instantly

---

## Explanation

### COPY vs Bind Mount

| COPY | Bind Mount |
|------|-----------|
| Build-time | Run-time |
| Image rebuild required | No rebuild |
| Immutable | Flexible |
| Production | Development |

### When Live Editing Is Useful

- UI fixes
- Development & testing
- Debugging
- Learning demos

### Immutability vs Flexibility

- Immutability ensures stability
- Flexibility enables fast changes
- Production prefers immutable images
- Development prefers bind mounts

---

## Deliverables
<img width="1902" height="1089" alt="Screenshot 2026-01-02 205244" src="https://github.com/user-attachments/assets/c4d39b05-4449-4988-82ad-1ced4228ce82" />
<img width="1919" height="1074" alt="Screenshot 2026-01-02 205332" src="https://github.com/user-attachments/assets/2eefb922-509a-43e1-bd8c-ba417541c4cb" />

---

## Short Explanation 

This task demonstrates Docker bind mounts to update static webpage content without rebuilding the image. Unlike COPY, which embeds files at build time, bind mounts allow live editing at runtime. This is useful during development and debugging as changes appear instantly. However, bind mounts reduce immutability, which is important in production. Hence, development favors flexibility while production favors immutable images.

---

## Final Summary

- Question 2 demonstrates Kubernetes Jobs for run-to-completion workloads
- Question 4 demonstrates Docker bind mounts for live content editing
