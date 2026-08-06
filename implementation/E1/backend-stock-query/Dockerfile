FROM node:20-alpine
WORKDIR /app
COPY package.json ./
COPY src ./src
COPY test ./test
RUN npm test
EXPOSE 8080
CMD ["node", "src/server.js"]
