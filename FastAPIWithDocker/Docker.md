# Install Docker

## For Linux

### Step 1: Update Package Information
#### Ubuntu
```bash
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io
```

#### Arch Linux
```bash
sudo pacman -Suy
sudo pacman -S docker
```

### Step 2: Verify Installation
```bash
docker --version
```

---

## For Windows

### Step 1: Download Docker Desktop
- Download Docker Desktop from the [official Docker website](https://www.docker.com/products/docker-desktop/).

### Step 2: Install Docker Desktop
1. Enable WSL 2 during installation.
2. Open PowerShell as an administrator and run:
   ```powershell
   wsl --install
   ```
3. Enable the Virtual Machine Platform:
   ```powershell
   Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
   ```
4. Set a username and password when prompted.
5. Update UNIX (WSL) after installation:
   ```bash
   sudo apt update && sudo apt upgrade
   ```

### Step 3: Add the Docker CLI Repository (Ubuntu on WSL)
1. Install required packages:
   ```bash
   sudo apt -y install apt-transport-https ca-certificates curl gnupg lsb-release
   ```

2. Add the Docker GPG key:
   ```bash
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
   ```

3. Add the Docker repository:
   ```bash
   echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   ```

4. Install Docker CLI:
   ```bash
   sudo apt install -y docker.io
   ```

### Step 4: Verify Installation
```bash
docker --version
```

### Step 5: Start Docker
```bash
sudo service docker start
sudo service docker status
docker run hello-world
```

### Step 6: Verify Docker in PowerShell
```powershell
wsl docker --version
```

---

# Docker Basics

### Start Docker Service
```bash
sudo systemctl start docker
sudo systemctl enable docker
```

### Display Docker Images
```bash
sudo docker images
```

### Show Running or Stopped Containers
```bash
sudo docker ps      # Show running containers
sudo docker ps -a   # Show all containers
```

### Stop a Docker Container
```bash
sudo docker stop <container_id>
```

### Build a Docker Image
```bash
docker build -t my-app:1.0 .
```
*(Run this command in the same directory as your `Dockerfile`.)*

### Remove a Docker Container
```bash
sudo docker rm <container_id>
```

### Remove a Docker Image
```bash
sudo docker rmi <image_id>
```

### Clean Up Unused Resources
```bash
sudo docker system prune
```

---

## Pushing an Image to Docker Hub

### Step 1: Log In to Docker Hub
```bash
sudo docker login
```
*(Provide your username and password or token.)*

### Step 2: Tag the Image
```bash
sudo docker tag <my_image:tag> <dockerhub_username>/<my_image:tag>
```

### Step 3: Push the Image to Docker Hub
```bash
sudo docker push <dockerhub_username>/<my_image:tag>
```