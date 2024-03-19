import { fileURLToPath, URL } from "node:url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  build: {
    outDir: "./dist/",

    rollupOptions: {
      output: {
        chunkFileNames: "static/vue-frontend-build/js/[name]-[hash].js",
        entryFileNames: "static/vue-frontend-build/js/[name]-[hash].js",

        assetFileNames: ({ name }) => {
          if (/\.(gif|jpe?g|png|svg|webp)$/.test(name ?? "")) {
            return "static/vue-frontend-build/images/[name]-[hash][extname]";
          }

          if (/\.css$/.test(name ?? "")) {
            return "static/vue-frontend-build/css/[name]-[hash][extname]";
          }

          if (/\.(woff|woff2)$/.test(name ?? "")) {
            return "static/vue-frontend-build/fonts/[name]-[hash][extname]";
          }

          // default value
          // ref: https://rollupjs.org/guide/en/#outputassetfilenames
          return "static/vue-frontend-build/[name][extname]";
        },
      },
    },
  },
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
});
