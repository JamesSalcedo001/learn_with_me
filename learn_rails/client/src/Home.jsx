import screenshot1 from "./Images/Screen Shot 2024-02-10 at 8.39.15 PM.png"
import screenshot2 from "./Images/Screen Shot 2024-02-10 at 8.45.29 PM.png"

function Home() {

    return (
        <div className="home">
            <h1>Here is an example of JSX syntax</h1>

            <br/>

            <img src={screenshot2}/>

            <br/>
            <br/>
            <p>JSX stands for JavaScript XML. It is a syntax extension for JS, and one can write a combination of HTML and JavaScript together, making development more efficient</p>
            
            <br/>

            <h1>Key Points of JSX</h1>
            <br/>

            <ul>
                <li>Elements: JSX elements look like HTML tags</li>
                <br/>

                <li>Attributes: One can use attributes with JSX elems just like HTML, however JSX uses camelCase naming convention instead. ex: 'class' becomes 'className' etc. </li>
                <br/>

                <li>Expressions: you can embed JavaScript expressions in JSX by wrapping them in curly braces</li>
                <br/>

                <li>Children: like HTML, JSX elements can have children</li>
            </ul>
            <br/>

            <h1>Converting HTML - JSX</h1>
            <br/>

            <p>Under the hood, JSX is translated into JS calls to React.createElement. These calls create objects that represent the DOM elements you want to create</p>
            <br/>

            <p>this JSX element below: </p>
            <br/>
            <br/>


            <img src={screenshot2}/>
            <br/>
            <br/>


            <p>translates to this under the hood: </p>
            <br/>
            <br/>


            <img src={screenshot1}/>

            <br/>

            <h1>React.createElement takes three arguments:</h1>
            <br/>

            <ul>
                <li>Tag name of element</li>
                <li>An object containing props and attributes</li>
                <li>The children of the element, and if there are multiple children, additional arguments are passed</li>
            </ul>

        </div>
    )
}

export default Home;