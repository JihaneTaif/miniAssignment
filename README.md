# ERP System - Complete Full-Stack Application

A modern, full-featured ERP (Enterprise Resource Planning) system built with Django REST Framework and Next.js.

## 🎉 Project Status: COMPLETE ✅

All phases have been successfully implemented!

---

## 📋 Features

### ✅ Phase 1: Backend Foundation
- **Database**: PostgreSQL (Neon Cloud)
- **Authentication**: JWT-based authentication with role-based access control
- **User Roles**: Admin, Manager, Agent, Viewer
- **Models**: Users, Leads, Clients, Products, Claims
- **Admin Panel**: Full Django admin interface

### ✅ Phase 2: API Development
- **34+ REST API Endpoints**
- **User Management**: Create, update, assign roles, reset password, deactivate
- **Leads Management**: Full CRUD, assign, convert to client, add comments
- **Clients Management**: Full CRUD, assign products, calculate income, activity history
- **Products Management**: Full CRUD with filtering
- **Claims Management**: Full CRUD, assign, update status, resolve, add comments
- **API Documentation**: Auto-generated Swagger UI

### ✅ Phase 3: Frontend Development
- **Modern UI**: Next.js 16 with Tailwind CSS v4
- **Responsive Design**: Mobile-first, works on all devices
- **Beautiful Animations**: Smooth transitions and micro-interactions
- **Complete Pages**:
  - Login page with JWT authentication
  - Dashboard with statistics and quick actions
  - Leads management with conversion
  - Clients management with card layout
  - Products catalog with active/inactive toggle
  - Claims tracking with status management
  - Users administration

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Node.js 18+
- PostgreSQL (Neon account)

### Backend Setup

1. **Navigate to backend directory**:
   ```bash
   cd backend
   ```

2. **Activate virtual environment**:
   ```bash
   .\venv\Scripts\activate
   ```

3. **Install dependencies** (already done):
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations** (already done):
   ```bash
   python manage.py migrate
   ```

5. **Start the server**:
   ```bash
   python manage.py runserver
   ```

   Backend will be available at: **http://127.0.0.1:8000**

### Frontend Setup

1. **Navigate to frontend directory**:
   ```bash
   cd frontend/front
   ```

2. **Install dependencies** (already done):
   ```bash
   npm install
   ```

3. **Create `.env.local` file**:
   ```env
   NEXT_PUBLIC_API_URL=http://127.0.0.1:8000/api/v1
   ```

4. **Start the development server**:
   ```bash
   npm run dev
   ```

   Frontend will be available at: **http://localhost:3000**

---

## 🔐 Default Credentials

Use your superuser credentials to login:
- **Email**: Your admin email
- **Password**: Your admin password

---

## 📚 API Documentation

### Swagger UI
Visit: **http://127.0.0.1:8000/api/docs/**

### API Endpoints

#### Authentication
- `POST /api/v1/auth/login/` - Login and get JWT tokens
- `POST /api/v1/auth/refresh/` - Refresh access token

#### Users (Admin Only)
- `GET /api/v1/users/` - List all users
- `POST /api/v1/users/` - Create new user
- `GET /api/v1/users/{id}/` - Get user details
- `PATCH /api/v1/users/{id}/` - Update user
- `POST /api/v1/users/{id}/assign-role/` - Assign role
- `POST /api/v1/users/{id}/reset-password/` - Reset password
- `POST /api/v1/users/{id}/deactivate/` - Deactivate user

#### Leads
- `GET /api/v1/leads/` - List leads
- `POST /api/v1/leads/` - Create lead
- `GET /api/v1/leads/{id}/` - Get lead details
- `PATCH /api/v1/leads/{id}/` - Update lead
- `DELETE /api/v1/leads/{id}/` - Delete lead
- `POST /api/v1/leads/{id}/assign/` - Assign to user
- `POST /api/v1/leads/{id}/convert/` - Convert to client
- `POST /api/v1/leads/{id}/add-comment/` - Add comment

#### Clients
- `GET /api/v1/clients/` - List clients
- `POST /api/v1/clients/` - Create client
- `GET /api/v1/clients/{id}/` - Get client details
- `PATCH /api/v1/clients/{id}/` - Update client
- `DELETE /api/v1/clients/{id}/` - Delete client
- `POST /api/v1/clients/{id}/assign-products/` - Assign products
- `GET /api/v1/clients/{id}/total-income/` - Get total income
- `GET /api/v1/clients/{id}/activity-history/` - Get activity history

#### Products
- `GET /api/v1/products/` - List products
- `POST /api/v1/products/` - Create product
- `GET /api/v1/products/{id}/` - Get product details
- `PATCH /api/v1/products/{id}/` - Update product
- `DELETE /api/v1/products/{id}/` - Delete product

#### Claims
- `GET /api/v1/claims/` - List claims
- `POST /api/v1/claims/` - Create claim
- `GET /api/v1/claims/{id}/` - Get claim details
- `PATCH /api/v1/claims/{id}/` - Update claim
- `DELETE /api/v1/claims/{id}/` - Delete claim
- `POST /api/v1/claims/{id}/assign/` - Assign to user
- `POST /api/v1/claims/{id}/update-status/` - Update status
- `POST /api/v1/claims/{id}/resolve/` - Resolve claim
- `POST /api/v1/claims/{id}/add-comment/` - Add comment

---

## 🎨 Frontend Features

### Design System
- **Modern Color Palette**: Professional blue/purple gradient theme
- **Responsive Layout**: Works on mobile, tablet, and desktop
- **Smooth Animations**: Fade-in, slide-in, and hover effects
- **Custom Components**: Buttons, cards, badges, inputs, modals
- **Dark Mode Ready**: Theme variables prepared for dark mode

### Pages

#### 1. Login Page (`/login`)
- Beautiful gradient background
- Email and password authentication
- JWT token management
- Error handling

#### 2. Dashboard (`/dashboard`)
- Statistics overview (leads, clients, products, claims)
- Quick actions
- System overview with progress bars
- Real-time data

#### 3. Leads (`/dashboard/leads`)
- Table view with all leads
- Create, edit, delete operations
- Convert lead to client
- Status badges
- Source tracking

#### 4. Clients (`/dashboard/clients`)
- Card-based layout
- Full contact information
- Activity and income buttons
- Industry tracking

#### 5. Products (`/dashboard/products`)
- Product catalog
- Price display
- Active/inactive toggle
- Category management

#### 6. Claims (`/dashboard/claims`)
- Priority indicators
- Status management
- Client association
- Resolution tracking

#### 7. Users (`/dashboard/users`)
- User management table
- Role assignment
- Password reset
- User deactivation

---

## 🏗️ Tech Stack

### Backend
- **Framework**: Django 5.2.9
- **API**: Django REST Framework
- **Authentication**: JWT (djangorestframework-simplejwt)
- **Database**: PostgreSQL (Neon)
- **CORS**: django-cors-headers
- **Documentation**: drf-spectacular (Swagger UI)

### Frontend
- **Framework**: Next.js 16
- **Language**: TypeScript
- **Styling**: Tailwind CSS v4
- **HTTP Client**: Axios
- **Icons**: React Icons
- **Date Handling**: date-fns

---

## 📁 Project Structure

```
ERPproject/
├── backend/
│   ├── back/                 # Django project settings
│   ├── users/                # User management app
│   ├── leads/                # Leads management app
│   ├── clients/              # Clients management app
│   ├── products/             # Products management app
│   ├── claims/               # Claims management app
│   ├── manage.py
│   ├── requirements.txt
│   └── .env                  # Database credentials
│
└── frontend/front/
    ├── app/
    │   ├── login/            # Login page
    │   ├── dashboard/        # Dashboard and all pages
    │   ├── globals.css       # Global styles
    │   └── layout.tsx        # Root layout
    ├── lib/
    │   ├── api.ts            # Axios instance
    │   ├── services.ts       # API service functions
    │   └── types.ts          # TypeScript interfaces
    ├── package.json
    └── .env.local            # API URL configuration
```

---

## 🔧 Configuration

### Backend (.env)
```env
DB_NAME=ERP
DB_USER=neondb_owner
DB_PASSWORD=npg_NuGiQ9B6lwER
DB_HOST=ep-blue-glitter-ahr9e4ec-pooler.c-3.us-east-1.aws.neon.tech
DB_PORT=5432
```

### Frontend (.env.local)
```env
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000/api/v1
```

---

## 🎯 User Roles & Permissions

- **Admin**: Full system access, user management
- **Manager**: Manage leads, clients, products, claims
- **Agent**: Handle assigned leads and claims
- **Viewer**: Read-only access

---

## 🚀 Deployment

### Backend (Django)
1. Set `DEBUG = False` in settings.py
2. Configure `ALLOWED_HOSTS`
3. Collect static files: `python manage.py collectstatic`
4. Use a production server (Gunicorn, uWSGI)
5. Set up HTTPS

### Frontend (Next.js)
1. Build the application: `npm run build`
2. Start production server: `npm start`
3. Or deploy to Vercel (recommended)

---

## 📝 Notes

- The backend is running on **http://127.0.0.1:8000**
- The frontend is running on **http://localhost:3000**
- API documentation is available at **http://127.0.0.1:8000/api/docs/**
- All passwords are hashed using Django's default password hasher
- JWT tokens expire after 1 hour (configurable in settings.py)
- CORS is configured for localhost development

---

## 🎉 What's Implemented

✅ Complete backend with 5 Django apps
✅ 34+ REST API endpoints
✅ JWT authentication with automatic token refresh
✅ Role-based access control
✅ PostgreSQL database (Neon Cloud)
✅ Full frontend with 7 pages
✅ Responsive design
✅ Modern UI with animations
✅ Complete CRUD operations for all entities
✅ API documentation (Swagger UI)
✅ Error handling
✅ Form validation

---

## 📧 Support

For issues or questions, refer to:
- Backend API docs: http://127.0.0.1:8000/api/docs/
- API Documentation: `backend/API_DOCUMENTATION.md`

---

**Built with ❤️ using Django REST Framework and Next.js**
