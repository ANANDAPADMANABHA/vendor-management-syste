# Vendor Management System with Performance Metrics

This repository contains the source code for a Vendor Management System (VMS) developed using Django and Django REST Framework. The system allows for the management of vendor profiles, tracking of purchase orders, and calculation of vendor performance metrics.

## Installation

### Prerequisites

- Python 3.9
- Django
- Django REST Framework

### Steps

1. **Clone the repository:**
   git clone https://github.com/yourusername/vendor-management-system.git

2. **Install dependencies:**
   pip install -r requirements.txt

3. **Run migrations:**
   python manage.py migrate

4. **Create a superuser (admin):**
   python manage.py createsuperuser

5. **Start the development server:**
   python manage.py runserver

6. **Access the application at** `http://localhost:8000`.

## API Documentation

The API endpoints are documented below:

- **Vendor Endpoints:**
  - POST /api/vendors/: Create a new vendor.
  - GET /api/vendors/: List all vendors.
  - GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.
  - PUT /api/vendors/{vendor_id}/: Update a vendor's details.
  - DELETE /api/vendors/{vendor_id}/: Delete a vendor.

- **Purchase Order Endpoints:**
  - POST /api/purchase_orders/: Create a purchase order.
  - GET /api/purchase_orders/: List all purchase orders with optional filtering.
  - GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
  - PUT /api/purchase_orders/{po_id}/: Update a purchase order.
  - DELETE /api/purchase_orders/{po_id}/: Delete a purchase order.

- **Vendor Performance Endpoint:**
  - GET /api/vendors/{vendor_id}/performance: Retrieve a vendor's performance metrics.

## Postman Collection

For easy testing and interaction with the API endpoints, you can use the Postman collection provided [here](https://www.postman.com/speeding-astronaut-535841/workspace/vendor-management-system/collection/24765234-b7af1994-1760-4ac5-b17a-34a63d1da2a9?action=share&creator=24765234).

## Testing

To run the test suite, execute the following command:

python manage.py test

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/new-feature`).
6. Create a new pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This project was developed as part of a Django Developer Assignment.
