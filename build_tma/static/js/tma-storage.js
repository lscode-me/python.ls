/**
 * LSCode TMA - Telegram Cloud Storage Integration
 * 
 * Uses Telegram WebApp CloudStorage API to persist quiz results
 * and progress data.
 */

const TMAStorage = {
    // Storage key prefixes
    PREFIX: 'lscode_',
    QUIZ_PREFIX: 'quiz_',
    PROGRESS_PREFIX: 'progress_',
    PREFS_KEY: 'user_preferences',
    
    /**
     * Check if Telegram CloudStorage is available
     */
    isAvailable() {
        return window.Telegram?.WebApp?.CloudStorage !== undefined;
    },
    
    /**
     * Get Telegram CloudStorage instance
     */
    getStorage() {
        if (!this.isAvailable()) {
            console.warn('Telegram CloudStorage not available, using localStorage fallback');
            return null;
        }
        return window.Telegram.WebApp.CloudStorage;
    },
    
    /**
     * Generate storage key for quiz result
     */
    getQuizKey(courseId, moduleId) {
        return `${this.PREFIX}${this.QUIZ_PREFIX}${courseId}_${moduleId}`;
    },
    
    /**
     * Generate storage key for course progress
     */
    getProgressKey(courseId) {
        return `${this.PREFIX}${this.PROGRESS_PREFIX}${courseId}`;
    },
    
    /**
     * Save quiz result to cloud storage
     */
    async saveQuizResult(courseId, moduleId, result) {
        const key = this.getQuizKey(courseId, moduleId);
        const data = {
            ...result,
            timestamp: new Date().toISOString(),
            attempts: (result.attempts || 0) + 1,
        };
        
        const storage = this.getStorage();
        
        if (storage) {
            return new Promise((resolve, reject) => {
                storage.setItem(key, JSON.stringify(data), (error, success) => {
                    if (error) {
                        console.error('CloudStorage error:', error);
                        // Fallback to localStorage
                        localStorage.setItem(key, JSON.stringify(data));
                        resolve(false);
                    } else {
                        resolve(success);
                    }
                });
            });
        } else {
            // Fallback to localStorage
            localStorage.setItem(key, JSON.stringify(data));
            return true;
        }
    },
    
    /**
     * Get quiz result from cloud storage
     */
    async getQuizResult(courseId, moduleId) {
        const key = this.getQuizKey(courseId, moduleId);
        const storage = this.getStorage();
        
        if (storage) {
            return new Promise((resolve, reject) => {
                storage.getItem(key, (error, value) => {
                    if (error || !value) {
                        // Try localStorage fallback
                        const local = localStorage.getItem(key);
                        resolve(local ? JSON.parse(local) : null);
                    } else {
                        resolve(JSON.parse(value));
                    }
                });
            });
        } else {
            const local = localStorage.getItem(key);
            return local ? JSON.parse(local) : null;
        }
    },
    
    /**
     * Get all quiz results for a course
     */
    async getCourseQuizResults(courseId) {
        const storage = this.getStorage();
        const prefix = `${this.PREFIX}${this.QUIZ_PREFIX}${courseId}_`;
        const results = {};
        
        if (storage) {
            return new Promise((resolve, reject) => {
                storage.getKeys((error, keys) => {
                    if (error || !keys || keys.length === 0) {
                        // Try localStorage
                        for (let i = 0; i < localStorage.length; i++) {
                            const key = localStorage.key(i);
                            if (key.startsWith(prefix)) {
                                const moduleId = key.replace(prefix, '');
                                results[moduleId] = JSON.parse(localStorage.getItem(key));
                            }
                        }
                        resolve(results);
                        return;
                    }
                    
                    const relevantKeys = keys.filter(k => k.startsWith(prefix));
                    if (relevantKeys.length === 0) {
                        resolve(results);
                        return;
                    }
                    
                    storage.getItems(relevantKeys, (error, values) => {
                        if (error) {
                            resolve(results);
                            return;
                        }
                        
                        for (const [key, value] of Object.entries(values)) {
                            if (value) {
                                const moduleId = key.replace(prefix, '');
                                results[moduleId] = JSON.parse(value);
                            }
                        }
                        resolve(results);
                    });
                });
            });
        } else {
            // localStorage fallback
            for (let i = 0; i < localStorage.length; i++) {
                const key = localStorage.key(i);
                if (key.startsWith(prefix)) {
                    const moduleId = key.replace(prefix, '');
                    results[moduleId] = JSON.parse(localStorage.getItem(key));
                }
            }
            return results;
        }
    },
    
    /**
     * Save course progress
     */
    async saveProgress(courseId, progress) {
        const key = this.getProgressKey(courseId);
        const data = {
            ...progress,
            lastUpdated: new Date().toISOString(),
        };
        
        const storage = this.getStorage();
        
        if (storage) {
            return new Promise((resolve, reject) => {
                storage.setItem(key, JSON.stringify(data), (error, success) => {
                    if (error) {
                        localStorage.setItem(key, JSON.stringify(data));
                        resolve(false);
                    } else {
                        resolve(success);
                    }
                });
            });
        } else {
            localStorage.setItem(key, JSON.stringify(data));
            return true;
        }
    },
    
    /**
     * Get all progress data
     */
    async getProgress() {
        const storage = this.getStorage();
        const prefix = `${this.PREFIX}${this.PROGRESS_PREFIX}`;
        const progress = {};
        
        if (storage) {
            return new Promise((resolve, reject) => {
                storage.getKeys((error, keys) => {
                    if (error || !keys || keys.length === 0) {
                        // localStorage fallback
                        for (let i = 0; i < localStorage.length; i++) {
                            const key = localStorage.key(i);
                            if (key.startsWith(prefix)) {
                                const courseId = key.replace(prefix, '');
                                progress[courseId] = JSON.parse(localStorage.getItem(key));
                            }
                        }
                        resolve(progress);
                        return;
                    }
                    
                    const relevantKeys = keys.filter(k => k.startsWith(prefix));
                    if (relevantKeys.length === 0) {
                        resolve(progress);
                        return;
                    }
                    
                    storage.getItems(relevantKeys, (error, values) => {
                        if (error) {
                            resolve(progress);
                            return;
                        }
                        
                        for (const [key, value] of Object.entries(values)) {
                            if (value) {
                                const courseId = key.replace(prefix, '');
                                progress[courseId] = JSON.parse(value);
                            }
                        }
                        resolve(progress);
                    });
                });
            });
        } else {
            for (let i = 0; i < localStorage.length; i++) {
                const key = localStorage.key(i);
                if (key.startsWith(prefix)) {
                    const courseId = key.replace(prefix, '');
                    progress[courseId] = JSON.parse(localStorage.getItem(key));
                }
            }
            return progress;
        }
    },
    
    /**
     * Save user preferences
     */
    async savePreferences(prefs) {
        const key = `${this.PREFIX}${this.PREFS_KEY}`;
        const storage = this.getStorage();
        
        if (storage) {
            return new Promise((resolve, reject) => {
                storage.setItem(key, JSON.stringify(prefs), (error, success) => {
                    if (error) {
                        localStorage.setItem(key, JSON.stringify(prefs));
                        resolve(false);
                    } else {
                        resolve(success);
                    }
                });
            });
        } else {
            localStorage.setItem(key, JSON.stringify(prefs));
            return true;
        }
    },
    
    /**
     * Get user preferences
     */
    async getPreferences() {
        const key = `${this.PREFIX}${this.PREFS_KEY}`;
        const storage = this.getStorage();
        
        if (storage) {
            return new Promise((resolve, reject) => {
                storage.getItem(key, (error, value) => {
                    if (error || !value) {
                        const local = localStorage.getItem(key);
                        resolve(local ? JSON.parse(local) : {});
                    } else {
                        resolve(JSON.parse(value));
                    }
                });
            });
        } else {
            const local = localStorage.getItem(key);
            return local ? JSON.parse(local) : {};
        }
    },
    
    /**
     * Clear all stored data
     */
    async clearAll() {
        const storage = this.getStorage();
        
        if (storage) {
            return new Promise((resolve, reject) => {
                storage.getKeys((error, keys) => {
                    if (error || !keys) {
                        resolve(false);
                        return;
                    }
                    
                    const lscodeKeys = keys.filter(k => k.startsWith(this.PREFIX));
                    if (lscodeKeys.length === 0) {
                        resolve(true);
                        return;
                    }
                    
                    storage.removeItems(lscodeKeys, (error) => {
                        resolve(!error);
                    });
                });
            });
        }
        
        // Clear localStorage
        const keysToRemove = [];
        for (let i = 0; i < localStorage.length; i++) {
            const key = localStorage.key(i);
            if (key.startsWith(this.PREFIX)) {
                keysToRemove.push(key);
            }
        }
        keysToRemove.forEach(k => localStorage.removeItem(k));
        return true;
    }
};

// Export for use in other modules
window.TMAStorage = TMAStorage;
