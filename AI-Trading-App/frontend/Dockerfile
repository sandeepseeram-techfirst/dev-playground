FROM node:20-alpine

WORKDIR /app

COPY package.json package-lock.json ./

# Install dependencies (ignoring scripts to avoid permission issues in some setups, but usually standard install is fine)
RUN npm install

COPY . .

# Build the Next.js application
RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
