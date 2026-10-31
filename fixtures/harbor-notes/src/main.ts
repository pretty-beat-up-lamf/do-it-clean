import { createStore } from "./notes/store";

const store = createStore();
document.querySelector("#count")!.textContent = String(store.count());
