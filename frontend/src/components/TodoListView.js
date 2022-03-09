import TodoItem from './Todo.js'

function TodoView(props) {
    return (
        <div>
            <ul>
                {props.todoList.map((todo) => <TodoItem todo={todo} />)}
            </ul>
        </div>
    )
}


export default TodoView;