# How can I create a Kanban board using ReactJS?
// plain

Kanban boards are a popular way to manage tasks, and ReactJS is a great tool to create them. To create a Kanban board with ReactJS, you can use a library such as [react-beautiful-dnd](https://github.com/atlassian/react-beautiful-dnd).

First, you need to install the library with:

```
npm install react-beautiful-dnd
```

Then, you can create a Kanban board using the following code:

```
import React, { useState } from 'react'
import { DragDropContext, Droppable, Draggable } from 'react-beautiful-dnd'

const KanbanBoard = () => {
  const [items, setItems] = useState([
    { id: 'item-1', content: 'Task 1' },
    { id: 'item-2', content: 'Task 2' },
    { id: 'item-3', content: 'Task 3' },
  ])

  const onDragEnd = (result) => {
    const { destination, source, draggableId } = result

    if (!destination) {
      return
    }

    if (
      destination.droppableId === source.droppableId &&
      destination.index === source.index
    ) {
      return
    }

    const start = items[source.index]
    const finish = items[destination.index]

    setItems([
      ...items.slice(0, source.index),
      finish,
      ...items.slice(source.index + 1, destination.index),
      start,
      ...items.slice(destination.index + 1),
    ])
  }

  return (
    <DragDropContext onDragEnd={onDragEnd}>
      <Droppable droppableId="droppable">
        {(provided) => (
          <div
            {...provided.droppableProps}
            ref={provided.innerRef}
          >
            {items.map((item, index) => (
              <Draggable key={item.id} draggableId={item.id} index={index}>
                {(provided) => (
                  <div
                    ref={provided.innerRef}
                    {...provided.draggableProps}
                    {...provided.dragHandleProps}
                  >
                    {item.content}
                  </div>
                )}
              </Draggable>
            ))}
            {provided.placeholder}
          </div>
        )}
      </Droppable>
    </DragDropContext>
  )
}

export default KanbanBoard
```

This code creates a Kanban board with three tasks ("Task 1", "Task 2", and "Task 3"). The `onDragEnd` function is used to update the state when an item is moved. The `Draggable` component is used to wrap each task item, allowing it to be dragged and dropped.

The output of this code is a Kanban board with three tasks that can be reordered by dragging and dropping them.

Parts of the code:

- `npm install react-beautiful-dnd`: Installs the react-beautiful-dnd library.
- `DragDropContext`: Wraps the Kanban board and provides the drag and drop context.
- `Droppable`: Wraps the list of tasks and provides the droppable context.
- `Draggable`: Wraps each task item and provides the draggable context.
- `onDragEnd`: Updates the state when an item is moved.

## Helpful links

- [react-beautiful-dnd](https://github.com/atlassian/react-beautiful-dnd): Library used to create a Kanban board with ReactJS.
- [React Docs](https://reactjs.org/docs): Official React documentation.

onelinerhub: [How can I create a Kanban board using ReactJS?](https://onelinerhub.com/reactjs/how-can-i-create-a-kanban-board-using-reactjs)