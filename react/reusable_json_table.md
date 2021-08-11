## Example
```JSX
function GenericTable(props) {
	const { tdata } = props

	return (
		<table>
			<thead>
				{tdata.length > 0 && (
					Object.keys(tdata[0]).map((key, keyIndex) => (
						<th key={keyIndex}>{key}</th>
					))
				)}
			</thead>
			<tbody>
				{tdata.length > 0 && ( 
					tdata.map((row, rowIndex) => (
						<tr key={rowIndex}>
							{Object.keys(tdata[0]).map((key, keyIndex) => (
								<td key={`${rowIndex}_${keyIndex}`}>{row.[key]}</td>
							))}
						</tr>
					))
				)}
			</tbody>
		</table>
	)
}
```

This React component takes an array of JSON data and creates an HTML table based on the keys and values in a given object. 