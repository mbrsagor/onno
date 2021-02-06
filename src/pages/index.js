import styles from '../styles/Home.module.css';
import Layout from '../components/layout/Layout';
import SearchInput from '../components/Searchinput/Searchinput';
import CountriesTable from '../components/CountriesTable/CountriesTable';

export default function Home({countries}) {
  console.log(countries);
  return <Layout>
    <div className={styles.counts}>Found {countries.length} Country</div>
    <SearchInput placeholder="Search filter by name" />
    <CountriesTable countries={countries} />
  </Layout>
}


export const getStaticProps = async () => {
  const res = await fetch("https://restcountries.eu/rest/v2/all");
  const countries = await res.json();
  return {
    props: {
      countries
    }
  }
}
