# How can I use D3.js to create a Kanban board?
// plain

Using D3.js, a Kanban board can be created by defining a hierarchical data structure, then mapping this data structure to SVG elements. An example of this is shown below:

```
const data = {
    name: 'Root',
    children: [
        {
            name: 'To Do',
            children: [
                { name: 'Task 1' },
                { name: 'Task 2' },
            ]
        },
        {
            name: 'In Progress',
            children: [
                { name: 'Task 3' },
            ]
        },
        {
            name: 'Done',
            children: [
                { name: 'Task 4' },
            ]
        }
    ]
};

const svg = d3.select('svg');

const g = svg.append('g');

const treemap = d3.tree().size([svg.attr('width'), svg.attr('height')]);

const root = d3.hierarchy(data);

const treeData = treemap(root);

const links = g.selectAll('.link')
    .data(treeData.links())
    .enter().append('path')
    .attr('class', 'link')
    .attr('d', d3.linkHorizontal()
        .x(d => d.y)
        .y(d => d.x)
    );

const nodes = g.selectAll('.node')
    .data(treeData.descendants())
    .enter().append('g')
    .attr('class', d => 'node' + (d.children ? ' node--internal' : ' node--leaf'))
    .attr('transform', d => 'translate(' + d.y + ',' + d.x + ')');

nodes.append('circle')
    .attr('r', 2.5);

nodes.append('text')
    .attr('dy', 3)
    .attr('x', d => d.children ? -8 : 8)
    .style('text-anchor', d => d.children ? 'end' : 'start')
    .text(d => d.data.name);
```

This code will generate an SVG element with a Kanban board structure, as shown below:

![Kanban board](kanban-board.png)

## Code explanation


1. Define the data structure: This is done by creating a hierarchical data structure, where each node has a `name` and an array of `children`.
2. Select the SVG element: This is done using `d3.select('svg')`.
3. Create the tree layout: This is done using `d3.tree()`.
4. Create the links: This is done using `d3.linkHorizontal()`.
5. Create the nodes: This is done using `d3.hierarchy()` and `d3.descendants()`.
6. Create the circles: This is done using `d3.append('circle')`.
7. Create the text: This is done using `d3.append('text')`.

## Helpful links

- [D3.js Documentation](https://github.com/d3/d3/wiki)
- [Tree Layout](https://github.com/d3/d3-hierarchy#tree)
- [Link Generator](https://github.com/d3/d3-shape#link_linkHorizontal)

onelinerhub: [How can I use D3.js to create a Kanban board?](https://onelinerhub.com/javascript-d3/how-can-i-use-d--js-to-create-a-kanban-board)