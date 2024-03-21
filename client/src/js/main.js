import { createApp } from "vue";
import App from "../App.vue";
import router from "../router";

// BOOTSTRAP Import our custom CSS
import "../scss/styles.scss";

// BOOTSTRAP Import all of Bootstrap's JS
import * as bootstrap from "bootstrap";

const app = createApp(App);

app.use(router);

app.mount("#app");
