# AWS ECS Fargate CI/CD Pipeline

This project demonstrates a deployment of a **Python Flask** application using **Amazon ECS Fargate**. The infrastructure is defined as Code (IaC) using **Terraform**, and the application lifecycle is fully automated via a **GitHub Actions** CI/CD pipeline.

---

## 1. Architecture

The project implements a highly available, multi-AZ (Availability Zone) architecture to ensure reliability and scalability.



### Technical Flow
1.  **CI/CD Trigger:** GitHub Actions triggers on push to `main`, running linting and unit tests.
2.  **Containerization:** Upon success, it builds a Docker image and pushes it to **Amazon ECR**.
3.  **Deployment:** **ECS Fargate** pulls the new image and performs a rolling update.
4.  **Traffic Management:** Traffic is routed via an **Application Load Balancer (ALB)** across two public subnets for high availability.

---

## 2. Infrastructure as Code (Terraform)

The infrastructure is managed through a modular Terraform setup. The deployment follows three critical stages:

| Stage | Command | Description |
| :--- | :--- | :--- |
| **Initialize** | `terraform init` | Downloads providers and sets up the backend. |
| **Plan** | `terraform plan` | Previews the resources to be created. |
| **Apply** | `terraform apply` | Provisions VPC, ALB, ECS Cluster, and Security Groups. |

---

## 3. Runbook (Operational Guide)

### Deployment Instructions
1.  **Infrastructure:** Navigate to the `/terraform` directory and run:
    ```bash
    terraform apply --auto-approve
    ```
2.  **Application:** Push changes to the `main` branch of your repository.
3.  **Verification:**
    * Check the **GitHub Actions** tab for a "Success" status.
    * Visit the `app_url` output provided by Terraform.

### Rollback Procedures
* **Auto-Rollback:** ECS is configured with a **Deployment Circuit Breaker**. If a new container fails health checks, it automatically reverts to the previous version.
* **Manual Rollback:** To force a revert to a specific stable image:
    ```bash
    aws ecs update-service --cluster py-app-cluster --service py-app-service --rollback
    ```

### Monitoring & Logs
* **Application Logs:** Available in **CloudWatch** under the log group `/ecs/ecr-fargate-py-app`.
* **Health Checks:** View the **Target Group** status in the AWS Console to ensure tasks are marked as `Healthy`.

---

## 4. Troubleshooting

| Symptom | Probable Cause | Fix |
| :--- | :--- | :--- |
| **ALB 503 Error** | Tasks are crashing or failing to start. | Check the ECS Service "Events" tab. |
| **Pipeline Failure** | Linting or Unit Tests failed. | Run `flake8` and `pytest` locally to debug. |
| **Image Pull Error** | IAM role lacks ECR permissions. | Verify `ecs_task_execution_role` in `iam.tf`. |
| **Health Check 404** | Port mismatch in configuration. | Ensure `app.py` runs on the port defined in `ecs.tf`. |

---