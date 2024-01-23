import { writable } from "svelte/store";

// Store values.
// This is the task we are dragging.
export const currentlyDraggingTodoIndex = writable(null);
export const taskItemDraggable = writable(true);
// This is the current places where the task is.
export const currentDragPosition = writable(null);

// Functions for the store values.
export const toggleTaskItemDraggable = () => {
  taskItemDraggable.update((value) => !value);
}
