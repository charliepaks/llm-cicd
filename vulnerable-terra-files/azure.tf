# main.tf

# Azure Provider Configuration
provider "azurerm" {
  features {}
}

# Create a Storage Account with anonymous access enabled
resource "azurerm_storage_account" "unsafe_storage_account" {
  name                     = "unsaferawstorage"
  resource_group_name      = "unsafe-rg"
  location                 = "eastus"
  account_tier             = "Standard"
  account_replication_type = "LRS"

  # Enable anonymous access to blobs
  blob_public_access_enabled = true
}

# Create a Virtual Machine with default credentials and no Network Security Group
resource "azurerm_virtual_machine" "unsafe_vm" {
  name                  = "unsafe-vm"
  resource_group_name   = "unsafe-rg"
  location              = "eastus"
  vm_size               = "Standard_B1ms"

  # Use hard-coded admin password (insecure)
  admin_username = "adminuser"
  admin_password = "P@ssw0rd123"  # Never hard-code passwords

  # No Network Security Group attached, leaving ports open
  network_interface_ids = [azurerm_network_interface.unsafe_nic.id]
}

# Create a Network Interface without a Network Security Group
resource "azurerm_network_interface" "unsafe_nic" {
  name                = "unsafe-nic"
  resource_group_name = "unsafe-rg"
  location            = "eastus"

  ip_configuration {
    name                          = "primary"
    subnet_id                     = azurerm_subnet.unsafe_subnet.id
    private_ip_address_allocation = "Dynamic"
  }
}

# Create a Subnet without a Network Security Group
resource "azurerm_subnet" "unsafe_subnet" {
  name                 = "unsafe-subnet"
  resource_group_name  = "unsafe-rg"
  virtual_network_name = azurerm_virtual_network.unsafe_vnet.name
  address_prefixes     = ["10.0.1.0/24"]
}

# Create a Virtual Network
resource "azurerm_virtual_network" "unsafe_vnet" {
  name                = "unsafe-vnet"
  resource_group_name = "unsafe-rg"
  location            = "eastus"
  address_space       = ["10.0.0.0/16"]
}