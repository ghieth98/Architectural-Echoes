FROM node:latest

WORKDIR /app

# Copy the package.json and package-lock.json files separately to leverage Docker layer caching
COPY package*.json ./
RUN npm install

# Copy the rest of the frontend code
COPY . .

# Expose the port on which Vue.js will run
EXPOSE 8080

# Start the Vue.js app
CMD ["npm", "run", "dev"]