import { writable } from "svelte/store";

// Store values.
export const currentlyDraggingTodoIndex = writable(null);
export const taskItemDraggable = writable(true);

// Functions for the store values.
export const toggleTaskItemDraggable = () => {
  taskItemDraggable.update((value) => !value);
}
