const { defineConfig } = require('cypress');

module.exports = defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      // Configure other node events here
    },
    baseUrl: 'http://localhost:8000',
    viewportWidth: 1280,
    viewportHeight: 720,
    // Força o navegador a usar pt-BR
    env: {
      locale: 'pt-BR'
    },
  },
  chromeWebSecurity: false, // Se necessário para formulários
});
