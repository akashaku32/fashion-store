// Main JavaScript for Elegance Boutique

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all components
    initNavbar();
    initProductCards();
    initCart();
    initForms();
    initAnimations();
    initLazyLoading();
    initSearchModal();
});

// Navbar functionality
function initNavbar() {
    const navbar = document.querySelector('.navbar');
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    
    // Navbar scroll effect
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('navbar-scrolled');
        } else {
            navbar.classList.remove('navbar-scrolled');
        }
    });
    
    // Close mobile menu when clicking on a link
    document.querySelectorAll('.navbar-nav .nav-link').forEach(link => {
        link.addEventListener('click', function() {
            if (navbarCollapse.classList.contains('show')) {
                navbarToggler.click();
            }
        });
    });
}

// Product cards functionality
function initProductCards() {
    // Add to cart buttons
    document.querySelectorAll('.add-to-cart').forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const productId = this.dataset.productId;
            
            if (!productId) {
                console.error('Product ID not found');
                return;
            }
            
            const quantity = this.closest('.product-card')?.querySelector('input[name="quantity"]')?.value || 1;
            
            // Show loading state
            const originalContent = this.innerHTML;
            this.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
            this.disabled = true;
            
            // Add to cart
            fetch(`/add-to-cart/${productId}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                    'X-Requested-With': 'XMLHttpRequest',
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: `quantity=${quantity}`
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Show success state
                    this.innerHTML = '<i class="fas fa-check"></i>';
                    this.style.background = 'var(--sage-green)';
                    
                    // Update cart badge if exists
                    const cartBadge = document.querySelector('.badge');
                    if (cartBadge) {
                        cartBadge.textContent = data.cart_items_count;
                    }
                    
                    // Reset after 2 seconds
                    setTimeout(() => {
                        this.innerHTML = originalContent;
                        this.style.background = '';
                        this.disabled = false;
                    }, 2000);
                } else {
                    throw new Error('Failed to add to cart');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                // Show error state
                this.innerHTML = '<i class="fas fa-exclamation"></i>';
                this.style.background = '#dc3545';
                
                // Reset after 2 seconds
                setTimeout(() => {
                    this.innerHTML = originalContent;
                    this.style.background = '';
                    this.disabled = false;
                }, 2000);
            });
        });
    });
    
    // Product image hover effects
    document.querySelectorAll('.product-card').forEach(card => {
        const image = card.querySelector('.product-image img');
        if (image) {
            card.addEventListener('mouseenter', function() {
                image.style.transform = 'scale(1.1)';
            });
            
            card.addEventListener('mouseleave', function() {
                image.style.transform = 'scale(1)';
            });
        }
    });
}

// Cart functionality
function initCart() {
    // Update cart item quantity
    document.querySelectorAll('.quantity-controls input[type="number"]').forEach(input => {
        input.addEventListener('change', function() {
            const cartItemId = this.closest('.cart-item').dataset.cartItemId;
            const quantity = this.value;
            
            if (quantity > 0) {
                updateCartItem(cartItemId, quantity);
            }
        });
    });
    
    // Remove cart item
    document.querySelectorAll('.remove-cart-item').forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const cartItemId = this.dataset.cartItemId;
            
            if (confirm('Are you sure you want to remove this item?')) {
                removeFromCart(cartItemId);
            }
        });
    });
}

// Form functionality
function initForms() {
    // Form validation
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!validateForm(this)) {
                e.preventDefault();
            }
        });
    });
    
    // Real-time form validation
    document.querySelectorAll('.form-control').forEach(input => {
        input.addEventListener('blur', function() {
            validateField(this);
        });
        
        input.addEventListener('input', function() {
            clearFieldError(this);
        });
    });
    
    // Newsletter form
    const newsletterForm = document.querySelector('form[action*="newsletter-signup"]');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            submitNewsletter(this);
        });
    }
    
    // Password validation
    initPasswordValidation();
}

// Password validation functionality
function initPasswordValidation() {
    const password1 = document.querySelector('#id_password1');
    const password2 = document.querySelector('#id_password2');
    
    if (password1) {
        password1.addEventListener('input', function() {
            validatePassword(this.value);
        });
    }
    
    if (password2) {
        password2.addEventListener('input', function() {
            validatePasswordMatch();
        });
    }
}

function validatePassword(password) {
    const passwordField = document.querySelector('#id_password1');
    const feedback = document.querySelector('#password-feedback') || createPasswordFeedback();
    
    let errors = [];
    
    if (password.length < 8) {
        errors.push('Password must be at least 8 characters long');
    }
    
    if (!/[A-Za-z]/.test(password)) {
        errors.push('Password must contain at least one letter');
    }
    
    if (!/\d/.test(password)) {
        errors.push('Password must contain at least one number');
    }
    
    if (errors.length === 0) {
        feedback.innerHTML = '<div class="text-success small">✓ Password meets all requirements</div>';
        passwordField.classList.remove('is-invalid');
        passwordField.classList.add('is-valid');
    } else {
        feedback.innerHTML = errors.map(error => `<div class="text-danger small">• ${error}</div>`).join('');
        passwordField.classList.remove('is-valid');
        passwordField.classList.add('is-invalid');
    }
}

function validatePasswordMatch() {
    const password1 = document.querySelector('#id_password1').value;
    const password2 = document.querySelector('#id_password2').value;
    const password2Field = document.querySelector('#id_password2');
    const feedback = document.querySelector('#password-match-feedback') || createPasswordMatchFeedback();
    
    if (password2.length > 0) {
        if (password1 === password2) {
            feedback.innerHTML = '<div class="text-success small">✓ Passwords match</div>';
            password2Field.classList.remove('is-invalid');
            password2Field.classList.add('is-valid');
        } else {
            feedback.innerHTML = '<div class="text-danger small">• Passwords do not match</div>';
            password2Field.classList.remove('is-valid');
            password2Field.classList.add('is-invalid');
        }
    }
}

function createPasswordFeedback() {
    const feedback = document.createElement('div');
    feedback.id = 'password-feedback';
    feedback.className = 'mt-1';
    document.querySelector('#id_password1').parentNode.appendChild(feedback);
    return feedback;
}

function createPasswordMatchFeedback() {
    const feedback = document.createElement('div');
    feedback.id = 'password-match-feedback';
    feedback.className = 'mt-1';
    document.querySelector('#id_password2').parentNode.appendChild(feedback);
    return feedback;
}

// Animation initialization
function initAnimations() {
    // Intersection Observer for scroll animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // Observe elements for animation
    document.querySelectorAll('.product-card, .category-card, .feature-card').forEach(el => {
        observer.observe(el);
    });
}

// Lazy loading for images
function initLazyLoading() {
    const imageObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });
    
    document.querySelectorAll('img[data-src]').forEach(img => {
        imageObserver.observe(img);
    });
}

// Add to cart function
function addToCart(productId, quantity = 1) {
    const button = document.querySelector(`[data-product-id="${productId}"]`);
    const originalText = button.innerHTML;
    
    // Show loading state
    button.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
    button.disabled = true;
    
    fetch(`/add-to-cart/${productId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCSRFToken(),
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `quantity=${quantity}`
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Update cart count
            updateCartCount(data.cart_items_count);
            
            // Show success notification
            showNotification('Product added to cart!', 'success');
            
            // Add success animation
            button.innerHTML = '<i class="fas fa-check"></i>';
            setTimeout(() => {
                button.innerHTML = originalText;
                button.disabled = false;
            }, 1000);
        } else {
            throw new Error(data.message || 'Failed to add product to cart');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showNotification('Error adding product to cart', 'error');
        button.innerHTML = originalText;
        button.disabled = false;
    });
}

// Update cart item quantity
function updateCartItem(cartItemId, quantity) {
    fetch(`/update-cart-item/${cartItemId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCSRFToken(),
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `quantity=${quantity}`
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Update cart totals
            updateCartTotals(data.cart_total, data.cart_items_count);
            showNotification('Cart updated successfully', 'success');
        } else {
            throw new Error(data.message || 'Failed to update cart');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showNotification('Error updating cart', 'error');
        // Reload page to sync state
        window.location.reload();
    });
}

// Remove from cart
function removeFromCart(cartItemId) {
    fetch(`/remove-from-cart/${cartItemId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCSRFToken(),
            'X-Requested-With': 'XMLHttpRequest',
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Remove item from DOM
            const cartItem = document.querySelector(`[data-cart-item-id="${cartItemId}"]`);
            if (cartItem) {
                cartItem.style.animation = 'fadeOut 0.3s ease-out';
                setTimeout(() => {
                    cartItem.remove();
                    // Check if cart is empty
                    if (document.querySelectorAll('.cart-item').length === 0) {
                        showEmptyCart();
                    }
                }, 300);
            }
            
            showNotification('Item removed from cart', 'success');
        } else {
            throw new Error(data.message || 'Failed to remove item');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showNotification('Error removing item', 'error');
    });
}

// Update cart count in navbar
function updateCartCount(count) {
    const cartBadge = document.querySelector('.navbar .badge');
    if (cartBadge) {
        cartBadge.textContent = count;
        cartBadge.style.animation = 'pulse 0.5s ease-in-out';
    }
}

// Update cart totals
function updateCartTotals(total, count) {
    // Update cart count
    updateCartCount(count);
    
    // Update cart total if on cart page
    const cartTotal = document.querySelector('.cart-total');
    if (cartTotal) {
        cartTotal.textContent = `$${total}`;
    }
}

// Show empty cart message
function showEmptyCart() {
    const cartContainer = document.querySelector('.cart-items');
    if (cartContainer) {
        cartContainer.innerHTML = `
            <div class="empty-cart text-center py-5">
                <i class="fas fa-shopping-cart fa-4x text-muted mb-4"></i>
                <h4 class="text-muted mb-3">Your cart is empty</h4>
                <p class="text-muted mb-4">Looks like you haven't added any items to your cart yet.</p>
                <a href="/products/" class="btn btn-primary btn-lg">
                    <i class="fas fa-shopping-bag me-2"></i>Start Shopping
                </a>
            </div>
        `;
    }
}

// Newsletter subscription
function submitNewsletter(form) {
    const email = form.querySelector('input[name="email"]').value;
    const button = form.querySelector('button[type="submit"]');
    const originalText = button.innerHTML;
    
    // Show loading state
    button.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
    button.disabled = true;
    
    fetch('/newsletter-signup/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCSRFToken(),
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `email=${encodeURIComponent(email)}`
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showNotification(data.message, 'success');
            form.reset();
        } else {
            showNotification(data.message, 'error');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showNotification('Error subscribing to newsletter', 'error');
    })
    .finally(() => {
        button.innerHTML = originalText;
        button.disabled = false;
    });
}

// Form validation
function validateForm(form) {
    let isValid = true;
    const requiredFields = form.querySelectorAll('[required]');
    
    requiredFields.forEach(field => {
        if (!validateField(field)) {
            isValid = false;
        }
    });
    
    return isValid;
}

// Field validation
function validateField(field) {
    const value = field.value.trim();
    const fieldType = field.type;
    let isValid = true;
    let errorMessage = '';
    
    // Required field check
    if (field.hasAttribute('required') && !value) {
        isValid = false;
        errorMessage = 'This field is required';
    }
    
    // Email validation
    if (fieldType === 'email' && value) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(value)) {
            isValid = false;
            errorMessage = 'Please enter a valid email address';
        }
    }
    
    // Password validation
    if (fieldType === 'password' && value) {
        if (value.length < 8) {
            isValid = false;
            errorMessage = 'Password must be at least 8 characters long';
        }
    }
    
    // Show/hide error
    if (isValid) {
        clearFieldError(field);
    } else {
        showFieldError(field, errorMessage);
    }
    
    return isValid;
}

// Show field error
function showFieldError(field, message) {
    clearFieldError(field);
    
    field.classList.add('is-invalid');
    
    const errorDiv = document.createElement('div');
    errorDiv.className = 'invalid-feedback';
    errorDiv.textContent = message;
    
    field.parentNode.appendChild(errorDiv);
}

// Clear field error
function clearFieldError(field) {
    field.classList.remove('is-invalid');
    
    const errorDiv = field.parentNode.querySelector('.invalid-feedback');
    if (errorDiv) {
        errorDiv.remove();
    }
}

// Show notification
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    notification.style.cssText = 'top: 100px; right: 20px; z-index: 9999; min-width: 300px; max-width: 400px;';
    notification.innerHTML = `
        <div class="d-flex align-items-center">
            <i class="fas fa-${getNotificationIcon(type)} me-2"></i>
            <span>${message}</span>
        </div>
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    document.body.appendChild(notification);
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        if (notification.parentNode) {
            notification.remove();
        }
    }, 5000);
}

// Get notification icon
function getNotificationIcon(type) {
    const icons = {
        success: 'check-circle',
        error: 'exclamation-circle',
        warning: 'exclamation-triangle',
        info: 'info-circle'
    };
    return icons[type] || 'info-circle';
}

// Get CSRF token
function getCSRFToken() {
    const token = document.querySelector('[name=csrfmiddlewaretoken]');
    return token ? token.value : '';
}

// Utility functions
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// Add CSS animations
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeOut {
        from { opacity: 1; transform: translateX(0); }
        to { opacity: 0; transform: translateX(-100%); }
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
    
    .navbar-scrolled {
        background-color: rgba(255, 255, 255, 0.98) !important;
        box-shadow: 0 2px 20px rgba(0, 0, 0, 0.1);
    }
    
    .lazy {
        opacity: 0;
        transition: opacity 0.3s;
    }
    
    .lazy.loaded {
        opacity: 1;
    }
`;
document.head.appendChild(style);

// Search modal functionality
function initSearchModal() {
    const searchModal = document.getElementById('searchModal');
    const modalSearchInput = document.getElementById('modal-search-input');
    
    if (searchModal && modalSearchInput) {
        // Focus on input when modal opens
        searchModal.addEventListener('shown.bs.modal', function() {
            modalSearchInput.focus();
        });
        
        // Handle Enter key in modal search
        modalSearchInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                e.preventDefault();
                document.getElementById('modal-search-form').submit();
            }
        });
        
        // Clear input when modal is hidden
        searchModal.addEventListener('hidden.bs.modal', function() {
            modalSearchInput.value = '';
        });
    }
}
