# Monitoring WebApps with Docker and GitHub Actions

A project consisting of three simple web applications built with Flask, Golang, and Node.js, each running independently. 
Deployment is fully automated through a GitHub Actions CI/CD pipeline to an AWS EC2 instance using Docker. This project focuses on monitoring the EC2 instance and the three web applications across different technology stacks.


---

## Project Structure
```
webapps/
├── website/
│   ├── flask/
│   ├── golang/
│   ├── node.js/
│   └── docker-compose.yml
├── .github/
└── docker.sh
```

---

## How to Use

### 1. Launch Your EC2 Instance

- Make sure you open the following ports in your Security Group:
  - **80** (HTTP)
  - **5000** (Flask app)
  - **3000** (Node.js app)
  - **8080** (Golang app)
  - **9090** (Prometheus UI)
  - **9000** (Node Exporter)
  - **3001** (Grafana UI)

- SSH into your EC2 instance and run the following commands:

```bash
ssh-keygen -t rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
chmod 600 ~/.ssh/id_rsa
cat ~/.ssh/id_rsa
```
Copy the content of your private key (output from cat ~/.ssh/id_rsa) and save it for GitHub Secret setup.
Make sure you copy from -----BEGIN OPENSSH PRIVATE KEY----- until -----END OPENSSH PRIVATE KEY-----.

### 2. Set Up Github Secret
- Create a repository on GitHub.
- o to Settings → Secrets and Variables → Actions → New repository secret.
- Add the following secrets:
    - DEPLOY_SERVER_IP: your EC2 public IP address.
    - DEPLOY_USER_UBUNTU: your EC2 username (e.g., ubuntu if you are using the Ubuntu AMI).
    - SSH_KEY_UBUNTU: your private SSH key (the output of cat ~/.ssh/id_rsa).

### 3. Push Your Code
- Download the project code and push it into your GitHub repository.

### 4. Trigger The Deployment
- Open the Actions tab in your GitHub repository.
- You will see the deployment process triggered automatically.
- Wait until the process is completed successfully.

### 5. Verify Deployment
- Open your browser and check if the apps are running:
  | Service | URL |
  | :----- | :----- |
  | Flask | http://your-ec2-ip:5000 |
  | Node | http://your-ec2-ip:3000 |
  | Golang | http://your-ec2-ip:8080 |
  | Prometheus | http://your-ec2-ip:9090 |
  | Grafana | http://your-ec2-ip:3001 |
  | node_exporter | http://your-ec2-ip:9000 |
- In Prometheus UI:
  - Go to Status → Targets
  - If the scrape targets are healthy, the status will show UP.

### 6. Set Up Grafana
- Configure Grafana by adding Prometheus as a data source.
- Start creating dashboards to monitor your services.

### 7. Check Running Containers
- If you want to make sure the containers are running, run the following commands on your EC2 instance:
  ```
  sudo docker ps ( running containers)
  sudo docker ps -a (Shows all containers, even the exited ones.)
  ```
- You should see 6 running containers, as listed in the table above.

---

### Build With
- Docker & Docker Compose
- AWS EC2
- Flask
- Golang
- Node.js
- Github Actions
- Prometheus
- Grafana
- Node_Exporter
