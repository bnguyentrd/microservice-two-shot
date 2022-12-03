import { BrowserRouter, Routes, Route } from 'react-router-dom';
import MainPage from './MainPage';
import Nav from './Nav';
import HatsList from './HatsList';
import HatsForm from './HatsForm';
import ShoesList from './ShoesList';
import ShoesForm from './ShoesForm';

function App(props) {
  // if (props.shoes === undefined) {
  //   return null;
  // }
  return (
    <BrowserRouter>
      <Nav />
      <div className="container">
        <Routes>
          <Route path="/" element={<MainPage />} />
          <Route path="hats" element={<HatsList />} />
            <Route path="new" element={<HatsForm />} />
          <Route path="shoes" element={<ShoesList shoes={props.shoes} />} />
            <Route path="new" element={<ShoesForm />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
