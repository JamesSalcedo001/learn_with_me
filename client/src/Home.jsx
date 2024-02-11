
function Home() {
    const element = <h3 className="greeting">Hello, World</h3>

    return (
        <div>
            <h1>Here is an example of JSX syntax, on line 3, and below is the result</h1>
            <>{element}</>
            <p>JSX stands for JavaScript XML. It is a syntax extension for JS, and one can write a combination of HTML and JavaScript together, making development more efficient</p>
            
            <h1>Key Points of JSX</h1>
            <ol>
                <li>Elements: JSX elements look like HTML tags</li>
                <li>Attributes: One can use attributes with JSX elems just like HTML, however JSX uses camelCase naming convention instead. ex: 'class' becomes 'className' etc. </li>
            </ol>
        </div>
    )
}

export default Home;