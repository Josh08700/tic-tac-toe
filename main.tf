terraform {
  required_providers {
    render = {
      source  = "render-oss/render"
      version = "~> 1.3.0"
    }
  }
}

variable "render_api_key" {
  type        = string
  description = "Render API Key for authentication"
  sensitive   = true
}

provider "render" {
  api_key = var.render_api_key
}

# Define your Render Web Service
resource "render_web_service" "tictactoe" {
  name          = "tictactoe-nicegui"
  region        = "oregon" # Options: oregon, frankfurt, singapore, ohio
  plan          = "free"
  num_instances = 1

  # Source code repository and build configuration
  runtime_source = {
    docker = {
      repo_url        = "https://github.com/your-username/your-repo" # Update with your Git repo URL
      branch          = "main"
      dockerfile_path = "./Dockerfile"
      context         = "."
    }
  }

  # Top-level environment variables map
  env_vars = {
    PORT = {
      value = "8080"
    }
  }
}

output "service_url" {
  value       = render_web_service.tictactoe.url
  description = "The public web URL of your Tic-Tac-Toe application"
}