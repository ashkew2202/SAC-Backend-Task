# SAC-Backend-Task

## Overview

Welcome to the SAC Backend Task repository! This project demonstrates a robust backend API built with best practices in mind. Below you'll find setup instructions, usage details, and how to interact with the API using Postman.

---

## Features

- Swagger Documentation
- CRUD operations
- Error handling
- Environment configuration

---

## Getting Started

### Prerequisites

You can set them up by using the following command:-

```bash
pip install -r requirements.txt
```

### Installation

```bash
git clone https://github.com/yourusername/SAC-Backend-Task.git
cd SAC-Backend-Task
```

### Environment Setup

Create a `.env` file in the root directory and add your configuration:

```env
DJANGO_SECRET_KEY = "django-insecure-4@5%s2l5npdp4!)$rhi8&d($k3dqy*ze=0aronbdnghvk%a@e1"
```

### Running the Server

```bash
cd product
python3/py/python manage.py runserver 6969
```

The server will start on `http://localhost:6969`.

---

## API Documentation

All endpoints are documented with swagger and will be accessible at `https://localhost:6969/swagger` or `https://localhost:6969/redoc` and ready for testing via Postman.

### Using the Public Postman Collection

1. **Access the Collection:**  
    [Click here to view the SAC Backend Task Postman Collection](https://www.postman.com/anshpmk-1856750/workspace/sac-apis)

2. **Import to Postman:**  
    - Open Postman.
    - Click "Import" and paste the collection link above.
    - Start testing endpoints interactively.

3. **Environment Variables:**  
    - Set the `base_url` variable to `http://localhost:6969` (or your deployed URL).
    - Update authentication tokens as needed.

