import './App.css'
import MainWindow from './components/MainWindow'
import Navbar from './components/Navbar'

function App() {

  return (
    <>
    <div className='max-h-screen flex flex-col'>
      <Navbar/>
    </div>
    <MainWindow/>
    </>
  )
}

export default App
