resource "aws_ecr_repository" "app_repo" {
  name                 = "ecr-fargate-py-app"
  image_tag_mutability = "MUTABLE"
  force_delete         = true # Allows TF to delete the repo even if images are inside

  image_scanning_configuration {
    scan_on_push = true
  }
}

# # This output will show you the URL you need for your Docker login
# output "ecr_repository_url" {
#   value = aws_ecr_repository.app_repo.repository_url
# }