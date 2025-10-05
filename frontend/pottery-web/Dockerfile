FROM node:20-slim
WORKDIR /app

# Copy manifests first
COPY package*.json ./

# Install deps (devDependencies included)
# If lockfile is platform-mismatched, fall back to npm install
RUN npm ci || (rm -f package-lock.json && npm install)

# Copy the rest of the app
COPY . .

CMD ["npm", "run", "dev", "--", "--host"]
