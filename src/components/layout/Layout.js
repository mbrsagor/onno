import Head from 'next/head';
import styles from './Layout.module.css';

const Layout = ({children}) => {
    return (
        <div className={styles.container}>
        <Head>
            <title>Create Next App</title>
            <link rel="icon" href="/favicon.ico" />
        </Head>

        <main className={styles.main}>{children}</main>

        <footer className={styles.footer}>
            Footer
        </footer>
    </div>
    )
}
export default Layout;
