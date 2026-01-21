/**
 * LSCode TMA - Main JavaScript
 */

// Telegram WebApp instance
const tg = window.Telegram?.WebApp;

document.addEventListener('DOMContentLoaded', function() {
    // Initialize Telegram WebApp
    if (tg) {
        tg.ready();
        tg.expand();
        
        // Setup back button
        if (tg.BackButton) {
            // Show back button if not on home page
            if (window.location.pathname !== '/' && !window.location.pathname.endsWith('/index.html')) {
                tg.BackButton.show();
                tg.BackButton.onClick(() => {
                    history.back();
                });
            }
        }
        
        // Apply theme class based on color scheme
        if (tg.colorScheme === 'dark') {
            document.body.classList.add('tg-dark');
        }
        
        // Handle viewport changes
        tg.onEvent('viewportChanged', ({ isStateStable }) => {
            if (isStateStable) {
                document.documentElement.style.setProperty(
                    '--tg-viewport-stable-height', 
                    tg.viewportStableHeight + 'px'
                );
            }
        });
    }
    
    // Setup header back button
    const backBtn = document.querySelector('.back-btn');
    if (backBtn) {
        // Hide if on home page
        if (window.location.pathname === '/' || window.location.pathname.endsWith('/index.html')) {
            backBtn.style.visibility = 'hidden';
        }
    }
});

// Toggle menu (placeholder for future menu functionality)
function toggleMenu() {
    // Could show a bottom sheet menu
    if (tg) {
        tg.showAlert('Menu coming soon!');
    } else {
        alert('Menu coming soon!');
    }
}

// Navigate to URL
function navigateTo(url) {
    window.location.href = url;
}

// Open Telegram link
function openTelegramLink(url) {
    if (tg) {
        tg.openTelegramLink(url);
    } else {
        window.open(url, '_blank');
    }
}

// Show confirmation dialog
function showConfirm(message, callback) {
    if (tg && tg.showConfirm) {
        tg.showConfirm(message, callback);
    } else {
        const result = confirm(message);
        callback(result);
    }
}

// Show alert
function showAlert(message, callback) {
    if (tg && tg.showAlert) {
        tg.showAlert(message, callback);
    } else {
        alert(message);
        if (callback) callback();
    }
}

// Haptic feedback
function hapticFeedback(type = 'impact') {
    if (tg && tg.HapticFeedback) {
        switch (type) {
            case 'impact':
                tg.HapticFeedback.impactOccurred('medium');
                break;
            case 'success':
                tg.HapticFeedback.notificationOccurred('success');
                break;
            case 'error':
                tg.HapticFeedback.notificationOccurred('error');
                break;
            case 'warning':
                tg.HapticFeedback.notificationOccurred('warning');
                break;
            case 'selection':
                tg.HapticFeedback.selectionChanged();
                break;
        }
    }
}

// Close WebApp
function closeApp() {
    if (tg) {
        tg.close();
    } else {
        window.close();
    }
}

// Send data to bot
function sendDataToBot(data) {
    if (tg) {
        tg.sendData(JSON.stringify(data));
    } else {
        console.log('Would send to bot:', data);
    }
}

// Format date for display
function formatDate(isoString) {
    const date = new Date(isoString);
    return date.toLocaleDateString(undefined, {
        month: 'short',
        day: 'numeric',
        year: 'numeric'
    });
}

// Debounce function
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

// Export utilities
window.TMAUtils = {
    navigateTo,
    openTelegramLink,
    showConfirm,
    showAlert,
    hapticFeedback,
    closeApp,
    sendDataToBot,
    formatDate,
    debounce
};
