import { defineConfig } from 'cypress';

export default defineConfig({
  video: false,
  viewportWidth: 1280,
  viewportHeight: 720,
  defaultCommandTimeout: 5000,
  execTimeout: 60000,
  retries: {
    runMode: 2,
    openMode: 0,
  },
  chromeWebSecurity: false,
  e2e: {
    baseUrl: 'http://localhost:4200',
    specPattern: 'cypress/tests/**/**/*.feature',
  },
});