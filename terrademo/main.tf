terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.12.0"
    }
  }
}

provider "google" {
  project = "terraform-demo-411911"
  region  = "asia-south-east"#"us-central1"
}

resource "google_storage_bucket" "demo-bucket" {
  name          = "terraform-demo-411911-terra-bucket"
  location      = "US"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}