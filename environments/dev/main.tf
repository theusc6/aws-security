resource "aws_s3_bucket" "test_deploy_bucket" {
  bucket = "test-deploy-bucket"
  acl    = "private"

  versioning {
    enabled = true
  }

  # Enable server-side encryption by default
  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }

