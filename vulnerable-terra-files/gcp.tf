# main.tf

# GCP Provider Configuration
provider "google" {
  project = "your-gcp-project-id"
  region  = "us-central1"
}

# Create a Cloud Storage bucket with public access
resource "google_storage_bucket" "unsafe_bucket" {
  name          = "unsafe-public-bucket"
  location      = "US"

  # Enable public read and write access
  uniform_bucket_level_access = true
  iam_binding {
    role = "roles/storage.objectAdmin"
    members = [
      "allUsers"
    ]
  }
}

# Create a Compute Engine instance with no firewall rules
resource "google_compute_instance" "unsafe_instance" {
  name         = "unsafe-vm"
  machine_type = "f1-micro"
  zone         = "us-central1-a"

  # No network tags, defaults to allowing all traffic
  # No firewall rules defined, leaving ports open
}