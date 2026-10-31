import { expect, test } from "vitest";
import { createStore } from "../src/notes/store";

test("starts empty", () => {
  expect(createStore().count()).toBe(0);
});
