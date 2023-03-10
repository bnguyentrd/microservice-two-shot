import { BrowserRouter, Routes, Route } from 'react-router-dom';
import MainPage from './MainPage';
import Nav from './Nav';
import HatsList from './HatsList';
import HatsForm from './HatsForm';
import ShoesList from './ShoesList';
import ShoesForm from './ShoesForm';

function App(props) {
  if (props.hats === undefined && props.shoes === undefined) {
    return null;
  }

  return (
    <BrowserRouter>
      <Nav />
      <div className="container">
        <Routes>
          <Route path="/" element={<MainPage />} />
          <Route path="shoes" element={<ShoesList shoes={props.shoes} />} />
          <Route path="shoes/new" element={<ShoesForm />} />
          <Route path="hats" element={<HatsList hats={props.hats} />} />
          <Route path="hats/new" element={<HatsForm />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
