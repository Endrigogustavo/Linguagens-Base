import { useState } from 'react'
import viteLogo from '/vite.svg'
import './style.css'


function App() {
  return ( 
    <>
<main>
        <h1>Create Account</h1>
        <div class="alternative">
            <span>OR</span>
        </div>

        <form action="">
            <label for="name">
                <span>Name</span>
                <input type="text" />
            </label>

            <label for="email">
                <span>E-mail</span>
               <input type="text" />
            </label>

            <label for="password">
                <span>Password</span>
                <input type="text" />
            </label>
                <input type="submit" />
        </form>
    </main>
    </>
  )
}

export default App
