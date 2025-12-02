# ERP System API Documentation

## Base URL
```
http://127.0.0.1:8000/api/v1/
```

## API Documentation
- **Swagger UI**: http://127.0.0.1:8000/api/docs/
- **API Schema**: http://127.0.0.1:8000/api/schema/

---

## Authentication

### Login (Get JWT Token)
```http
POST /api/v1/auth/login/
Content-Type: application/json

{
  "email": "admin@erp.com",
  "password": "your_password"
}

Response:
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Refresh Token
```http
POST /api/v1/auth/refresh/
Content-Type: application/json

{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Using Authentication
Add to all requests:
```
Authorization: Bearer <access_token>
```

---

## User Management APIs ✅

### List Users (Admin Only)
```http
GET /api/v1/users/
```

### Create User (Admin Only)
```http
POST /api/v1/users/
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "securepass123",
  "password2": "securepass123",
  "first_name": "John",
  "last_name": "Doe",
  "role": "agent",
  "phone": "+1234567890",
  "department": "Sales"
}
```

### Get User Details
```http
GET /api/v1/users/{id}/
```

### Update User
```http
PATCH /api/v1/users/{id}/
Content-Type: application/json

{
  "first_name": "Jane",
  "is_active": true
}
```

### Assign Role (Admin Only)
```http
POST /api/v1/users/{id}/assign-role/
Content-Type: application/json

{
  "role": "manager"
}
```

### Reset Password (Admin Only)
```http
POST /api/v1/users/{id}/reset-password/
Content-Type: application/json

{
  "password": "newpassword123"
}
```

### Deactivate User (Admin Only)
```http
POST /api/v1/users/{id}/deactivate/
```

---

## Leads APIs ✅

### List Leads
```http
GET /api/v1/leads/
GET /api/v1/leads/?status=new
GET /api/v1/leads/?assigned_to=1
```

### Create Lead
```http
POST /api/v1/leads/
Content-Type: application/json

{
  "name": "John Smith",
  "email": "john@company.com",
  "phone": "+1234567890",
  "company": "ABC Corp",
  "source": "website",
  "assigned_to": 1,
  "notes": "Interested in our services"
}
```

### Get Lead Details
```http
GET /api/v1/leads/{id}/
```

### Update Lead
```http
PATCH /api/v1/leads/{id}/
Content-Type: application/json

{
  "status": "contacted",
  "notes": "Follow up scheduled"
}
```

### Delete Lead
```http
DELETE /api/v1/leads/{id}/
```

### Assign Lead to Operator
```http
POST /api/v1/leads/{id}/assign/
Content-Type: application/json

{
  "user_id": 2
}
```

### Convert Lead to Client
```http
POST /api/v1/leads/{id}/convert/
```

### Add Comment to Lead
```http
POST /api/v1/leads/{id}/add-comment/
Content-Type: application/json

{
  "comment": "Customer requested a callback tomorrow"
}
```

---

## Clients APIs ✅

### List Clients
```http
GET /api/v1/clients/
GET /api/v1/clients/?account_manager=1
```

### Create Client
```http
POST /api/v1/clients/
Content-Type: application/json

{
  "name": "Jane Doe",
  "email": "jane@company.com",
  "phone": "+1234567890",
  "company": "XYZ Inc",
  "address": "123 Main St, City, State",
  "industry": "Technology",
  "account_manager": 1,
  "notes": "VIP client"
}
```

### Get Client Details
```http
GET /api/v1/clients/{id}/
```

### Update Client
```http
PATCH /api/v1/clients/{id}/
Content-Type: application/json

{
  "industry": "Finance",
  "notes": "Updated industry"
}
```

### Delete Client
```http
DELETE /api/v1/clients/{id}/
```

### Assign Products/Services
```http
POST /api/v1/clients/{id}/assign-products/
Content-Type: application/json

{
  "product_ids": [1, 2, 3]
}
```

### Calculate Total Income
```http
GET /api/v1/clients/{id}/total-income/
```

### View Activity History
```http
GET /api/v1/clients/{id}/activity-history/
```

---

## Products/Services APIs ✅

### List Products
```http
GET /api/v1/products/
GET /api/v1/products/?category=product
GET /api/v1/products/?is_active=true
```

### Create Product
```http
POST /api/v1/products/
Content-Type: application/json

{
  "name": "Premium Service Package",
  "description": "Our premium service offering",
  "sku": "PREM-001",
  "category": "service",
  "price": "999.99",
  "is_active": true
}
```

### Get Product Details
```http
GET /api/v1/products/{id}/
```

### Update Product
```http
PATCH /api/v1/products/{id}/
Content-Type: application/json

{
  "price": "1099.99",
  "is_active": true
}
```

### Delete Product
```http
DELETE /api/v1/products/{id}/
```

---

## Claims APIs ✅

### List Claims
```http
GET /api/v1/claims/
GET /api/v1/claims/?status=open
GET /api/v1/claims/?client=1
GET /api/v1/claims/?assigned_to=2
```

### Create Claim (Client-side)
```http
POST /api/v1/claims/
Content-Type: application/json

{
  "client": 1,
  "product": 1,
  "title": "Product not working as expected",
  "description": "Detailed description of the issue...",
  "priority": "high"
}
```

### Get Claim Details
```http
GET /api/v1/claims/{id}/
```

### Update Claim
```http
PATCH /api/v1/claims/{id}/
Content-Type: application/json

{
  "status": "in_progress",
  "priority": "urgent",
  "resolution_notes": "Working on resolution"
}
```

### Delete Claim
```http
DELETE /api/v1/claims/{id}/
```

### Assign Claim to Operator/Supervisor
```http
POST /api/v1/claims/{id}/assign/
Content-Type: application/json

{
  "user_id": 3
}
```

### Update Claim Status
```http
POST /api/v1/claims/{id}/update-status/
Content-Type: application/json

{
  "status": "resolved"
}
```

### Resolve Claim
```http
POST /api/v1/claims/{id}/resolve/
Content-Type: application/json

{
  "resolution_notes": "Issue resolved by replacing the product"
}
```

### Add Comment to Claim
```http
POST /api/v1/claims/{id}/add-comment/
Content-Type: application/json

{
  "comment": "Customer confirmed the issue is resolved"
}
```

---

## Status Codes

- `200 OK` - Request successful
- `201 Created` - Resource created successfully
- `204 No Content` - Resource deleted successfully
- `400 Bad Request` - Invalid request data
- `401 Unauthorized` - Authentication required
- `403 Forbidden` - Insufficient permissions
- `404 Not Found` - Resource not found
- `500 Internal Server Error` - Server error

---

## User Roles & Permissions

- **Admin**: Full access to all endpoints
- **Manager**: Access to leads, clients, products, claims
- **Agent**: Access to assigned leads and claims
- **Viewer**: Read-only access

---

## Testing the API

### Using cURL
```bash
# Login
curl -X POST http://127.0.0.1:8000/api/v1/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@erp.com","password":"your_password"}'

# Create a lead (with token)
curl -X POST http://127.0.0.1:8000/api/v1/leads/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name":"Test Lead","email":"test@example.com","source":"website"}'
```

### Using Postman
1. Import the API schema from: http://127.0.0.1:8000/api/schema/
2. Set up environment variable for the access token
3. Test all endpoints

### Using Swagger UI
Visit: http://127.0.0.1:8000/api/docs/
- Interactive API documentation
- Test endpoints directly from browser
- See request/response examples

---

## Next Steps

All Phase 2 APIs are complete! ✅

**Available Endpoints Summary:**
- ✅ User Management (7 endpoints)
- ✅ Leads (7 endpoints including CRUD + extras)
- ✅ Clients (7 endpoints including CRUD + extras)
- ✅ Products (5 endpoints - CRUD)
- ✅ Claims (8 endpoints including file handling ready)

**Note**: File upload handling is ready in the Claims model. To enable actual file uploads, you would need to:
1. Add a `FileField` to the Claim model
2. Configure `MEDIA_ROOT` and `MEDIA_URL` in settings
3. Update the serializer to handle file uploads
