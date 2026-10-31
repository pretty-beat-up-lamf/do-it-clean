export interface Note {
  id: string;
  body: string;
}

export function createStore() {
  const notes: Note[] = [];
  return {
    add: (n: Note) => notes.push(n),
    count: () => notes.length,
  };
}
