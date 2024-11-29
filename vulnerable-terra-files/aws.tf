# main.tf

# AWS Provider Configuration
provider "aws" {
  region = "us-east-1"
}

# Create an S3 bucket with public read and write access
resource "aws_s3_bucket" "unsafe_bucket" {
  bucket = "unsafe-public-bucket"

  # Enable public read and write access
  acl = "public-read-write"

  # Allow anyone to upload and download objects
  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Principal = "*",
        Action = [
          "s3:GetObject",
          "s3:PutObject"
        ],
        Resource = "arn:aws:s3:::unsafe-public-bucket/*"
      }
    ]
  })
}

# Create an EC2 instance with hard-coded password and no security group restrictions
resource "aws_instance" "unsafe_instance" {
  ami           = "ami-0abcdef1234567890"  # Replace with actual AMI ID
  instance_type = "t2.micro"

  # Hard-coded password (insecure)
  user_data = <<-EOF
              #!/bin/bash
              echo "root:password123" | chpasswd
              EOF

  # No security group, defaults to allowing all traffic
}